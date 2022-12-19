using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Tab;
using GuitarCogApi.Services;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;

namespace GuitarCogApi.Controllers;

[ApiController]
[Route("[controller]")]
public class TabController : CheckAuthControllerBase
{
    private readonly TabService _tabService;
    private readonly FileService _fileService;

    public TabController(TabService tabService, UserManager<User> userManager, FileService fileService) :
        base(userManager)
    {
        _tabService = tabService;
        _fileService = fileService;
    }

    [HttpPost]
    [Authorize]
    [ProducesResponseType(typeof(AddTabRespDto), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> AddTab([FromForm] AddTabDto addTabDto)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));

        var (tab, response) = await _tabService.AddTab(addTabDto, user);
        if (response != null || tab == null)
            return BadRequest(response ?? new Response("Error", "Cannot add tab"));

        return Ok(new AddTabRespDto(_fileService.GetUrlByFileId(Request, tab.TabFile.Id)));
    }

    [HttpDelete("{tabId:long}")]
    [Authorize]
    [ProducesResponseType(typeof(AddTabRespDto), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> DeleteTab(long tabId)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));

        var (tab, response) = await _tabService.DeleteTab(tabId, user);
        if (response != null || tab == null)
            return BadRequest(response ?? new Response("Error", "Cannot delete tab"));

        return Ok(tabId);
    }

    [HttpDelete("/Moder/Tab/{tabId:long}")]
    [Authorize(Roles = $"{nameof(Role.SuperAdmin)},{nameof(Role.Moderator)}")]
    [ApiExplorerSettings(GroupName = "ModerTab")]
    [ProducesResponseType(typeof(AddTabRespDto), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> DeleteModerTab(long tabId)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));

        var (tab, response) = await _tabService.DeleteTab(tabId);
        if (response != null || tab == null)
            return BadRequest(response ?? new Response("Error", "Cannot delete tab."));

        return Ok(tabId);
    }

    [HttpGet]
    [ProducesResponseType(typeof(PagedResponse<TabListDto>), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<ActionResult<PagedResponse<TabListDto>>> GetTabs([FromQuery] TabFilter tabFilter)
    {
        var (user, _) = await CheckAuth();
        return Ok(await _tabService.GetTabs(Request, tabFilter, user));
    }

    [HttpGet("GetTabLimit")]
    [Authorize]
    [ProducesResponseType(typeof(PagedResponse<TabListDto>), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> GetTabLimit()
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));

        var tabs = await _tabService.GetTabLimit(user);

        return Ok(tabs);
    }
}