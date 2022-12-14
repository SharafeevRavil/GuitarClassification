using GuitarCogApi.Dtos;
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
public class TabController : ControllerBase
{
    private TabService _tabService;
    private UserManager<User> _userManager;
    private FileService _fileService;

    public TabController(TabService tabService, UserManager<User> userManager, FileService fileService)
    {
        _tabService = tabService;
        _userManager = userManager;
        _fileService = fileService;
    }

    [HttpPost]
    [Authorize]
    [ProducesResponseType(typeof(AddTabRespDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> AddTab([FromForm] AddTabDto addTabDto)
    {
        var username = User.Identity?.Name;
        if (username == null)
            return BadRequest(new Response("Error", "User not found"));
        
        var user = await _userManager.FindByNameAsync(username);
        if (user == null)
            return BadRequest(new Response("Error", "User not found"));
        
        var (tab, response) = await _tabService.AddTab(addTabDto, user);
        if (response != null || tab == null)
            return BadRequest(response ?? new Response("Error", "Cannot add tab"));

        return Ok(new AddTabRespDto(_fileService.GetUrlByFileId(Request, tab.TabFile.Id)));
    }

    [HttpGet]
    [ProducesResponseType(typeof(PagedResponse<TabListDto>),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<ActionResult<PagedResponse<TabListDto>>> GetTabs([FromQuery] TabFilter tabFilter)
    {
        var tabs = await _tabService.GetTabs(Request, tabFilter);

        return Ok(tabs);
    }
}