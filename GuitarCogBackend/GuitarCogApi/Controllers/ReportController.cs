using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Report;
using GuitarCogApi.Services;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;

namespace GuitarCogApi.Controllers;

/// <summary>
/// Контроллер жалоб, как отправки, так и работы с ними модераторами
/// </summary>
[ApiController]
[Route("[controller]")]
public class ReportController : CheckAuthControllerBase
{
    private readonly ReportService _reportService;

    public ReportController(UserManager<User> userManager, ReportService reportService) : base(userManager)
    {
        _reportService = reportService;
    }

    /// <summary>
    /// Эндпоинт отправки пользователем жалобы на табулатуру
    /// </summary>
    /// <param name="tabId"></param>
    /// <returns></returns>
    [HttpPost("{tabId:long}")]
    [Authorize]
    [ProducesResponseType(typeof(long), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> ReportTab(long tabId)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));

        var (report, response) = await _reportService.ReportTab(user, tabId);
        if (response != null || report == null)
            return BadRequest(response ?? new Response("Error", "Cannot subscribe. Try later."));

        return Ok(report.Id);
    }

    /// <summary>
    /// Эндпоинт получения модератором списка жалоб на табулатуры
    /// </summary>
    /// <param name="filter"></param>
    /// <returns></returns>
    [HttpGet("/Moder/Report")]
    [Authorize(Roles = $"{nameof(Role.SuperAdmin)},{nameof(Role.Moderator)}")]
    [ApiExplorerSettings(GroupName = "ModerReport")]
    [ProducesResponseType(typeof(PagedResponse<ReportListDto>), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> GetReports([FromQuery] ReportPagedFilter filter)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));
        
        return Ok(await _reportService.GetReports(Request, filter));
    }

    /// <summary>
    /// Эндпоинт отметки жалобы как просмотренной модератором
    /// </summary>
    /// <param name="reportId"></param>
    /// <returns></returns>
    [HttpPost("/Moder/Report/MarkAsViewed")]
    [Authorize(Roles = $"{nameof(Role.SuperAdmin)},{nameof(Role.Moderator)}")]
    [ApiExplorerSettings(GroupName = "ModerReport")]
    [ProducesResponseType(typeof(void), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> MarkAsViewed([FromQuery] long reportId)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));
        
        var response = await _reportService.MarkAsViewed(reportId);
        if (response != null) return BadRequest(response);
        return Ok();
    }
}