using System.IdentityModel.Tokens.Jwt;
using GuitarCogApi.Dtos.Auth;
using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Profile;
using GuitarCogApi.Services;
using GuitarCogData;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace GuitarCogApi.Controllers;

[ApiController]
[Route("[controller]")]
public class ProfileController : ControllerBase
{
    private readonly UserManager<User> _userManager;
    private readonly AuthService _authService;
    private readonly ApplicationDbContext _dbContext;
    private readonly FileService _fileService;

    public ProfileController(UserManager<User> userManager, AuthService authService, ApplicationDbContext dbContext, FileService fileService)
    {
        _userManager = userManager;
        _authService = authService;
        _dbContext = dbContext;
        _fileService = fileService;
    }
    
    [Authorize]
    [HttpPost("ChangePassword")]
    public async Task<IActionResult> ChangePassword(ChangePasswordDto dto)
    {
        var username = User.Identity?.Name;
        if (username == null)
            return BadRequest(new Response("Error", "User not found"));
        
        var user = await _userManager.FindByNameAsync(username);
        if (user == null)
            return BadRequest(new Response("Error", "User not found"));
        
        if(dto.OldPassword == dto.NewPassword)
            return BadRequest(new Response("Error", "Passwords are the same"));

        var result = await _userManager.ChangePasswordAsync(user, dto.OldPassword, dto.NewPassword);
        if (!result.Succeeded)
        {
            var errors = result.Errors
                .Select(x => $"[{x.Code}] {x.Description}")
                .Aggregate((a, b) => $"{a}\n{b}");
            return BadRequest(new Response("Error", $"Password change failed! Errors:\n{errors}"));
        }

        var (token, refreshToken) = await _authService.GenerateTokensPair(user);
        return Ok(new TokenDto(new JwtSecurityTokenHandler().WriteToken(token), token.ValidTo, refreshToken));
    }

    [Authorize]
    [HttpPost("ChangeEmail")]
    public async Task<IActionResult> ChangeEmail(ChangeEmailDto dto)
    {
        var username = User.Identity?.Name;
        if (username == null)
            return BadRequest(new Response("Error", "User not found"));
        
        var user = await _userManager.FindByNameAsync(username);
        if (user == null)
            return BadRequest(new Response("Error", "User not found"));
        
        if(user.Email == dto.NewEmail)
            return BadRequest(new Response("Error", "Current email is the same"));

        var otherUserWithEmail = await _userManager.FindByEmailAsync(dto.NewEmail);
        if(otherUserWithEmail != null)
            return BadRequest(new Response("Error", "Email is busy"));
        
        await _userManager.SetEmailAsync(user, dto.NewEmail);
        var emailConfirmationToken = await _userManager.GenerateEmailConfirmationTokenAsync(user);
        var result = await _userManager.ConfirmEmailAsync(user, emailConfirmationToken);
        if (!result.Succeeded)
        {
            var errors = result.Errors
                .Select(x => $"[{x.Code}] {x.Description}")
                .Aggregate((a, b) => $"{a}\n{b}");
            return BadRequest(new Response("Error", $"Email change failed! Errors:\n{errors}"));
        }

        var (token, refreshToken) = await _authService.GenerateTokensPair(user);
        return Ok(new TokenDto(new JwtSecurityTokenHandler().WriteToken(token), token.ValidTo, refreshToken));
    }

    [Authorize]
    [HttpPost("ChangeUsername")]
    public async Task<IActionResult> ChangeUsername(ChangeUsernameDto dto)
    {
        var username = User.Identity?.Name;
        if (username == null)
            return BadRequest(new Response("Error", "User not found"));
        
        var user = await _userManager.FindByNameAsync(username);
        if (user == null)
            return BadRequest(new Response("Error", "User not found"));
        
        if(username == dto.NewUsername)
            return BadRequest(new Response("Error", "Current username is the same"));

        var otherUserWithUsername = await _userManager.FindByEmailAsync(dto.NewUsername);
        if(otherUserWithUsername != null)
            return BadRequest(new Response("Error", "Username is busy"));
        
        var result = await _userManager.SetUserNameAsync(user, dto.NewUsername);
        if (!result.Succeeded)
        {
            var errors = result.Errors
                .Select(x => $"[{x.Code}] {x.Description}")
                .Aggregate((a, b) => $"{a}\n{b}");
            return BadRequest(new Response("Error", $"Username change failed! Errors:\n{errors}"));
        }

        var (token, refreshToken) = await _authService.GenerateTokensPair(user);
        return Ok(new TokenDto(new JwtSecurityTokenHandler().WriteToken(token), token.ValidTo, refreshToken));
    }

    [Authorize]
    [HttpGet("GetUserInfo")]
    public async Task<IActionResult> GetUserInfo()
    {
        var username = User.Identity?.Name;
        if (username == null)
            return BadRequest(new Response("Error", "User not found"));
        
        var user = await _dbContext.Users
            .Include(x => x.AvatarImage)
            .FirstOrDefaultAsync(x => x.UserName == username);
        if (user == null)
            return BadRequest(new Response("Error", "User not found"));

        
        var avatarUrl = user.AvatarImage != null 
            ? _fileService.GetUrlByFileId(Request, user.AvatarImage!.Id) 
            : "";

        var dto = new ProfileDto(user.Id, user.UserName, user.Email, avatarUrl);
        return Ok(dto);
    }

    [Authorize]
    [HttpPost("ChangeAvatar")]
    public async Task<IActionResult> ChangeAvatar(IFormFile image)
    {
        var username = User.Identity?.Name;
        if (username == null)
            return BadRequest(new Response("Error", "User not found"));
        
        var user = await _userManager.FindByNameAsync(username);
        if (user == null)
            return BadRequest(new Response("Error", "User not found"));

        var (img, error) = await _fileService.AddFileFromForm(image, 2);
        if (error != null || img == null)
            return BadRequest(error);

        user.AvatarImage = img;
        await _userManager.UpdateAsync(user);
        var avatarUrl = _fileService.GetUrlByFileId(Request, img.Id);
        
        return Ok(new {AvatarUrl = avatarUrl});
    }
}