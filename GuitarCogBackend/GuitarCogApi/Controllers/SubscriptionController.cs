using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Subscription;
using GuitarCogApi.Services;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;

namespace GuitarCogApi.Controllers;

[ApiController]
[Route("[controller]")]
public class SubscriptionController : ControllerBase
{
    private readonly SubscriptionService _subscriptionService;
    private readonly UserManager<User> _userManager;

    public SubscriptionController(SubscriptionService subscriptionService, UserManager<User> userManager)
    {
        _subscriptionService = subscriptionService;
        _userManager = userManager;
    }

    [HttpGet("Price")]
    [ProducesResponseType(typeof(List<SubscriptionPriceDto>),StatusCodes.Status200OK)]
    public Task<IActionResult> GetPrice([FromQuery] GetSubscriptionPriceDto getSubscriptionPriceDto)
    {
        getSubscriptionPriceDto.StartDate ??= DateTimeOffset.UtcNow;
        
        var list = _subscriptionService.GetPriceForPeriod(getSubscriptionPriceDto);
        return Task.FromResult<IActionResult>(Ok(list));
    }

    [Authorize]
    [HttpPost("Subscribe")]
    [ProducesResponseType(typeof(List<SubscriptionPriceDto>),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> Subscribe(SubscribeDto subscribeDto)
    {
        var username = User.Identity?.Name;
        if (username == null)
            return BadRequest(new Response("Error", "User not found"));
        
        var user = await _userManager.FindByNameAsync(username);
        if (user == null)
            return BadRequest(new Response("Error", "User not found"));
        
        
        subscribeDto.StartDate ??= DateTimeOffset.UtcNow;
        var (resultDto, response) = await _subscriptionService.Subscribe(user, subscribeDto);
        if (response != null || resultDto == null)
            return BadRequest(response ?? new Response("Error", "Cannot subscribe. Try later."));
        
        return Ok(resultDto);
    }
}