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
}