using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Subscription;
using GuitarCogApi.Services;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;

namespace GuitarCogApi.Controllers;

/// <summary>
/// Контроллер подписок
/// </summary>
[ApiController]
[Route("[controller]")]
public class SubscriptionController : CheckAuthControllerBase
{
    private readonly SubscriptionService _subscriptionService;

    public SubscriptionController(SubscriptionService subscriptionService, UserManager<User> userManager) : base(userManager)
    {
        _subscriptionService = subscriptionService;
    }

    /// <summary>
    /// Эндпонт получения стоимости подписки с указанными параметрами
    /// </summary>
    /// <param name="getSubscriptionPriceDto"></param>
    /// <returns></returns>
    [HttpGet("Price")]
    [ProducesResponseType(typeof(List<SubscriptionPriceDto>),StatusCodes.Status200OK)]
    public Task<IActionResult> GetPrice([FromQuery] GetSubscriptionPriceDto getSubscriptionPriceDto)
    {
        getSubscriptionPriceDto.StartDate ??= DateTimeOffset.UtcNow;
        
        var list = _subscriptionService.GetPriceForPeriod(getSubscriptionPriceDto);
        return Task.FromResult<IActionResult>(Ok(list));
    }

    /// <summary>
    /// Эндпоинт подписки пользователем на сервис
    /// </summary>
    /// <param name="subscribeDto"></param>
    /// <returns></returns>
    [Authorize]
    [HttpPost("Subscribe")]
    [ProducesResponseType(typeof(List<SubscriptionPriceDto>),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> Subscribe(SubscribeDto subscribeDto)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));

        subscribeDto.StartDate ??= DateTimeOffset.UtcNow;
        var (resultDto, response) = await _subscriptionService.Subscribe(user, subscribeDto);
        if (response != null || resultDto == null)
            return BadRequest(response ?? new Response("Error", "Cannot subscribe. Try later."));
        
        return Ok(resultDto);
    }

    /// <summary>
    /// Эндпоинт получения статуса подипски пользователя
    /// </summary>
    /// <param name="date"></param>
    /// <returns></returns>
    [Authorize]
    [HttpGet("CheckSubscribed")]
    [ProducesResponseType(typeof(SubscriptionInfoDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> CheckSubscribed(DateTimeOffset? date)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));
        
        date ??= DateTimeOffset.UtcNow;
        var subscribed = await _subscriptionService.CheckSubscribed(user, date.Value);
                
        return Ok(subscribed);
    }
}