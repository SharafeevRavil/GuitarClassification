using GuitarCogApi.Dtos.Ad;
using GuitarCogApi.Dtos.General;
using GuitarCogApi.Services;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;

namespace GuitarCogApi.Controllers;

[ApiController]
[Route("[controller]")]
public class AdController : ControllerBase
{
    private readonly UserManager<User> _userManager;
    private readonly AdService _adService;

    public AdController(UserManager<User> userManager, AdService adService)
    {
        _adService = adService;
        _userManager = userManager;
    }

    /// <remarks> Этот метод может не работать в сваггере, если включен адблок - тупо запросы блочит нахуй </remarks>
    /// <remarks> И сами странички тоже с адблоком не работают 😜 </remarks>
    [HttpGet("GetAds")]
    [ProducesResponseType(typeof(AdDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> GetAds([FromQuery] int count = 10)
    {
        var username = User.Identity?.Name;
        
        var isAuthenticated = username != null;
        if (isAuthenticated)
        {
            var user = await _userManager.FindByNameAsync(username!);
            if (user == null)
                return BadRequest(new Response("Error", "User not found"));

            var needToShow = await _adService.CheckNeedToShowAds(user);
            if (!needToShow)
                return Ok(new AdDto(false, null));
        }

        var ads = _adService.GetAvailableAds(Request, count);

        return Ok(new AdDto(true, ads));
    }
}