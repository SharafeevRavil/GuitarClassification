﻿using GuitarCogApi.Dtos.General;
using GuitarCogApi.Services;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;

namespace GuitarCogApi.Controllers;

[ApiController]
[Route("[controller]")]
public class ReportController : ControllerBase
{
    private readonly UserManager<User> _userManager;
    private readonly ReportService _reportService;

    public ReportController(UserManager<User> userManager, ReportService reportService)
    {
        _userManager = userManager;
        _reportService = reportService;
    }

    [HttpPost("{tabId:long}")]
    [Authorize]
    [ProducesResponseType(typeof(long), StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response), StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> ReportTab(long tabId)
    {
        var username = User.Identity?.Name;
        if (username == null)
            return BadRequest(new Response("Error", "User not found"));
        
        var user = await _userManager.FindByNameAsync(username);
        if (user == null)
            return BadRequest(new Response("Error", "User not found"));

        var (report, response) = await _reportService.ReportTab(user, tabId);
        if (response != null || report == null)
            return BadRequest(response ?? new Response("Error", "Cannot subscribe. Try later."));

        return Ok(report.Id);
    } 
}