using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Security.Cryptography;
using System.Text;
using GuitarCogApi.Dtos.Auth;
using GuitarCogApi.Dtos.General;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.IdentityModel.Tokens;

namespace GuitarCogApi.Controllers;

[ApiController]
[Route("[controller]")]
public class AuthController : ControllerBase
{
    private readonly UserManager<User> _userManager;
    private readonly AuthService _authService;

    public AuthController(UserManager<User> userManager, AuthService authService)
    {
        _userManager = userManager;
        _authService = authService;
    }

    [HttpPost("SignIn")]
    [ProducesResponseType(typeof(TokenDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<ActionResult<TokenDto>> SignIn([FromBody] SignInDto model)
    {
        var user = await _userManager.FindByNameAsync(model.Username);
        if (user == null || !await _userManager.CheckPasswordAsync(user, model.Password)) return Unauthorized();

        var (token, refreshToken) = await _authService.GenerateTokensPair(user);

        return Ok(new TokenDto(new JwtSecurityTokenHandler().WriteToken(token), token.ValidTo, refreshToken));
    }

    [HttpPost("SignUp")]
    [ProducesResponseType(typeof(TokenDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<ActionResult<TokenDto>> SignUp([FromBody] SignUpDto model)
    {
        var userExists = await _userManager.FindByNameAsync(model.Username);
        if (userExists != null)
            return BadRequest(new Response("Error", "User already exists!"));

        User user = new()
        {
            Email = model.Email,
            SecurityStamp = Guid.NewGuid().ToString(),
            UserName = model.Username
        };
        var result = await _userManager.CreateAsync(user, model.Password);
        if (!result.Succeeded)
        {
            var errors = result.Errors
                .Select(x => $"[{x.Code}] {x.Description}")
                .Aggregate((a, b) => $"{a}\n{b}");
            return StatusCode(StatusCodes.Status500InternalServerError,
                new Response("Error", $"User creation failed! Errors:\n{errors}"));
        }

        var (token, refreshToken) = await _authService.GenerateTokensPair(user);

        return Ok(new TokenDto(new JwtSecurityTokenHandler().WriteToken(token), token.ValidTo, refreshToken));
    }

    [HttpPost("RefreshToken")]
    [ProducesResponseType(typeof(TokenDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<ActionResult<TokenDto>> RefreshToken([FromBody] TokenPairDto tokenModel)
    {
        var accessToken = tokenModel.AccessToken;
        var refreshToken = tokenModel.RefreshToken;

        var principal = _authService.GetPrincipalFromExpiredToken(accessToken);
        if (principal == null)
            return BadRequest(new Response("Error", "Invalid access token or refresh token"));

        var username = principal.Identity!.Name;
        var user = await _userManager.FindByNameAsync(username!);

        if (user == null || user.RefreshToken != refreshToken || user.RefreshTokenExpiryTime <= DateTimeOffset.UtcNow)
            return BadRequest(new Response("Error", "Invalid access token or refresh token"));

        var (newToken, newRefreshToken) = await _authService.GenerateTokensPair(user);
        return Ok(new TokenDto(new JwtSecurityTokenHandler().WriteToken(newToken), newToken.ValidTo, newRefreshToken));
    }

    [Authorize]
    [HttpGet("CheckAuthorized")]
    [ProducesResponseType(typeof(AuthorizedDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<ActionResult<AuthorizedDto>> CheckAuthorized()
    {
        var username = User.Identity?.Name;
        if (username == null)
            return BadRequest(new Response("Error", "User not found"));
        
        var user = await _userManager.FindByNameAsync(username);
        if (user == null)
            return BadRequest(new Response("Error", "User not found"));
        return Ok(new AuthorizedDto(username));
    }
}