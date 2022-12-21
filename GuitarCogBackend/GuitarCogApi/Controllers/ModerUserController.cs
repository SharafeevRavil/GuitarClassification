using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Moder.ModerUser;
using GuitarCogApi.Dtos.ModerUser;
using GuitarCogApi.Services.Moder;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;

namespace GuitarCogApi.Controllers;

/// <summary>
/// Контроллер для управления пользователями модератором
/// </summary>
[ApiController]
[Route("Moder/User")]
public class ModerUserController : CheckAuthControllerBase
{
    private readonly ModerUserService _moderUserService;

    public ModerUserController(ModerUserService moderUserService, UserManager<User> userManager) : base(userManager)
    {
        _moderUserService = moderUserService;
    }

    /// <summary>
    /// Эндпоинт получения списка пользователей
    /// </summary>
    /// <param name="pagedFilter"></param>
    /// <returns></returns>
    [HttpGet]
    [Authorize(Roles = $"{nameof(Role.SuperAdmin)},{nameof(Role.Moderator)}")]
    [ProducesResponseType(typeof(PagedResponse<ModerUserListDto>), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> GetUsers([FromQuery] ModerUserPagedFilter pagedFilter)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));

        return Ok(await _moderUserService.GetUsers(pagedFilter));
    }

    /// <summary>
    /// Эндпоинт создания модератора главным админом
    /// </summary>
    /// <param name="createModerDto"></param>
    /// <returns>ID модера</returns>
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

    /// <summary>
    /// Эндпоинт получения информации о пользователе
    /// </summary>
    /// <param name="id"></param>
    /// <returns></returns>
    [HttpGet("{id}")]
    [Authorize(Roles = $"{nameof(Role.SuperAdmin)},{nameof(Role.Moderator)}")]
    [ProducesResponseType(typeof(ModerUserDto), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> GetUser(string id)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));
        
        var (userDto, response) = await _moderUserService.GetUser(Request, id);
        if (response != null || userDto == null)
            return BadRequest(response ?? new Response("Error", "Cannot get user. Try later."));
        return Ok(userDto);
    }

    [HttpPost("BanUser")]
    [Authorize(Roles = $"{nameof(Role.SuperAdmin)},{nameof(Role.Moderator)}")]
    [ProducesResponseType(typeof(void), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> BanUser([FromQuery] string userId)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));

        var response = await _moderUserService.BanUser(user, userId);
        if (response != null)
            return BadRequest(response);
        
        return Ok();
    }

    [HttpPost("UnbanUser")]
    [Authorize(Roles = $"{nameof(Role.SuperAdmin)},{nameof(Role.Moderator)}")]
    [ProducesResponseType(typeof(void), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> UnbanUser([FromQuery] string userId)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));

        var response = await _moderUserService.UnbanUser(user, userId);
        if (response != null)
            return BadRequest(response);
        
        return Ok();
    }
}