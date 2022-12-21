using GuitarCogApi.Dtos.Ad;
using GuitarCogApi.Dtos.General;
using GuitarCogApi.Services;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;

namespace GuitarCogApi.Controllers;

/// <summary>
/// Контроллер для получения рекламы
/// </summary>
[ApiController]
[Route("[controller]")]
public class AdController : CheckAuthControllerBase
{
    private readonly AdService _adService;

    public AdController(UserManager<User> userManager, AdService adService) : base(userManager)
    {
        _adService = adService;
    }

    /// <summary>
    /// Эндпоинт получения объявлений
    /// </summary>
    /// <returns>Список объявлений</returns>
    /// <remarks> Этот метод может не работать в сваггере, если включен адблок - тупо запросы блочит нахуй </remarks>
    /// <remarks> И сами странички тоже с адблоком не работают 😜 </remarks>
    [HttpGet("GetAds")]
    [ProducesResponseType(typeof(AdDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> GetAds([FromQuery] int count = 10)
    {
        var (user, _) = await CheckAuth();
        if (user != null)
        {
            var needToShow = await _adService.CheckNeedToShowAds(user);
            if (!needToShow)
                return Ok(new AdDto(false, null));
        }

        var ads = _adService.GetAvailableAds(Request, count);

        return Ok(new AdDto(true, ads));
    }
}