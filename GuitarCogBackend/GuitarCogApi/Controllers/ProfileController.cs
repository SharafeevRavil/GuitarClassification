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

/// <summary>
/// Контроллер действий с профилем
/// </summary>
[ApiController]
[Route("[controller]")]
public class ProfileController : CheckAuthControllerBase
{
    private readonly AuthService _authService;
    private readonly ApplicationDbContext _dbContext;
    private readonly FileService _fileService;

    public ProfileController(UserManager<User> userManager, AuthService authService, ApplicationDbContext dbContext, FileService fileService) : base(userManager)
    {
        _authService = authService;
        _dbContext = dbContext;
        _fileService = fileService;
    }
    
    [Authorize]
    [HttpPost("ChangePassword")]
    [ProducesResponseType(typeof(TokenDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> ChangePassword(ChangePasswordDto dto)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));
        
        if(dto.OldPassword == dto.NewPassword)
            return BadRequest(new Response("Error", "Passwords are the same"));

        var result = await UserManager.ChangePasswordAsync(user, dto.OldPassword, dto.NewPassword);
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
    [ProducesResponseType(typeof(TokenDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> ChangeEmail(ChangeEmailDto dto)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));
        
        if(user.Email == dto.NewEmail)
            return BadRequest(new Response("Error", "Current email is the same"));

        var otherUserWithEmail = await UserManager.FindByEmailAsync(dto.NewEmail);
        if(otherUserWithEmail != null)
            return BadRequest(new Response("Error", "Email is busy"));
        
        await UserManager.SetEmailAsync(user, dto.NewEmail);
        var emailConfirmationToken = await UserManager.GenerateEmailConfirmationTokenAsync(user);
        var result = await UserManager.ConfirmEmailAsync(user, emailConfirmationToken);
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
    [ProducesResponseType(typeof(TokenDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> ChangeUsername(ChangeUsernameDto dto)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));
        
        if(user.UserName == dto.NewUsername)
            return BadRequest(new Response("Error", "Current username is the same"));

        var otherUserWithUsername = await UserManager.FindByEmailAsync(dto.NewUsername);
        if(otherUserWithUsername != null)
            return BadRequest(new Response("Error", "Username is busy"));
        
        var result = await UserManager.SetUserNameAsync(user, dto.NewUsername);
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
    [ProducesResponseType(typeof(ProfileDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> GetUserInfo()
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));

        user = await _dbContext.Users
            .Include(x => x.AvatarImage)
            .FirstOrDefaultAsync(x => x.UserName == user.UserName);
        if (user == null)
            return BadRequest(new Response("Error", "User not found"));
        
        var avatarUrl = user.AvatarImage != null 
            ? _fileService.GetUrlByFileId(Request, user.AvatarImage!.Id) 
            : "";

        var dto = new ProfileDto(user.Id, user.UserName!, user.Email!, avatarUrl);
        return Ok(dto);
    }

    [Authorize]
    [HttpPost("ChangeAvatar")]
    [ProducesResponseType(typeof(AvatarDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> ChangeAvatar(IFormFile image)
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));

        var (img, error) = await _fileService.AddFileFromForm(image, 2);
        if (error != null || img == null)
            return BadRequest(error);

        user.AvatarImage = img;
        await UserManager.UpdateAsync(user);
        var avatarUrl = _fileService.GetUrlByFileId(Request, img.Id);
        
        return Ok(new AvatarDto(avatarUrl));
    }
}