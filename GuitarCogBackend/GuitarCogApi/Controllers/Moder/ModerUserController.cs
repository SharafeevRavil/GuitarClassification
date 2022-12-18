using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Moder.ModerUser;
using GuitarCogApi.Services.Moder;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace GuitarCogApi.Controllers.Moder;

[ApiController]
[Route("Moder/[controller]")]
public class ModerUserController : ControllerBase
{
    private readonly ModerUserService _moderUserService;

    public ModerUserController(ModerUserService moderUserService)
    {
        _moderUserService = moderUserService;
    }

    [HttpGet]
    [Authorize(Roles = $"{nameof(Role.SuperAdmin)},{nameof(Role.Moderator)}")]
    [ProducesResponseType(typeof(PagedResponse<ModerUserListDto>), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> GetUsers([FromQuery] PagedFilter pagedFilter) =>
        Ok(await _moderUserService.GetUsers(pagedFilter));

    [HttpPost]
    [Authorize(Roles = $"{nameof(Role.SuperAdmin)}")]
    [ProducesResponseType(typeof(string), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> CreateModer(CreateModerDto createModerDto)
    {
        var (user, response) = await _moderUserService.CreateModer(createModerDto);
        if (response != null || user == null)
            return BadRequest(response ?? new Response("Error", "Cannot create moder. Try later."));
        return Ok(user.Id);
    }

    [HttpGet("{id}")]
    [Authorize(Roles = $"{nameof(Role.SuperAdmin)},{nameof(Role.Moderator)}")]
    [ProducesResponseType(typeof(PagedResponse<ModerUserDto>), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> GetUser(string id)
    {
        var (user, response) = await _moderUserService.GetUser(Request, id);
        if (response != null || user == null)
            return BadRequest(response ?? new Response("Error", "Cannot get user. Try later."));
        return Ok(user);
    }
}