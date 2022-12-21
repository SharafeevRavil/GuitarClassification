using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Security.Cryptography;
using System.Text;
using GuitarCogApi.Dtos.Auth;
using GuitarCogApi.Dtos.General;
using GuitarCogApi.Services;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.IdentityModel.Tokens;

namespace GuitarCogApi.Controllers;

/// <summary>
/// Контроллер для аутентификации
/// </summary>
[ApiController]
[Route("[controller]")]
public class AuthController : CheckAuthControllerBase
{
    private readonly AuthService _authService;
    private readonly UserService _userService;

    public AuthController(UserManager<User> userManager, AuthService authService, UserService userService) : base(userManager)
    {
        _authService = authService;
        _userService = userService;
    }

    /// <summary>
    /// Эндпоинт входа 
    /// </summary>
    /// <param name="model">Dto входа</param>
    /// <returns>Пара токенов</returns>
    [HttpPost("SignIn")]
    [ProducesResponseType(typeof(TokenDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<ActionResult<TokenDto>> SignIn([FromBody] SignInDto model)
    {
        var user = await UserManager.FindByNameAsync(model.Username);
        if (user == null || !await UserManager.CheckPasswordAsync(user, model.Password)) return Unauthorized();

        if (user.IsBanned)
            return BadRequest(new Response("Error", "Your account was banned"));
        
        var (token, refreshToken) = await _authService.GenerateTokensPair(user);

        return Ok(new TokenDto(new JwtSecurityTokenHandler().WriteToken(token), token.ValidTo, refreshToken));
    }

    /// <summary>
    /// Эндпоинт регистрации
    /// </summary>
    /// <param name="model">dto регистрации</param>
    /// <returns>Пара токенов</returns>
    [HttpPost("SignUp")]
    [ProducesResponseType(typeof(TokenDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<ActionResult<TokenDto>> SignUp([FromBody] SignUpDto model)
    {
        var (user, response) = await _userService.CreateUser(model.Username, model.Email, model.Password);
        if (response != null || user == null)
            return BadRequest(response ?? new Response("Error", "Cannot sign up. Try later."));

        var (token, refreshToken) = await _authService.GenerateTokensPair(user);

        return Ok(new TokenDto(new JwtSecurityTokenHandler().WriteToken(token), token.ValidTo, refreshToken));
    }

    /// <summary>
    /// Эндпоинт обновления токена
    /// </summary>
    /// <param name="tokenModel">Токены</param>
    /// <returns>Новая пара токенов</returns>
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
        var user = await UserManager.FindByNameAsync(username!);

        if (user == null || user.RefreshToken != refreshToken || user.RefreshTokenExpiryTime <= DateTimeOffset.UtcNow)
            return BadRequest(new Response("Error", "Invalid access token or refresh token"));

        var (newToken, newRefreshToken) = await _authService.GenerateTokensPair(user);
        return Ok(new TokenDto(new JwtSecurityTokenHandler().WriteToken(newToken), newToken.ValidTo, newRefreshToken));
    }

    /// <summary>
    /// Эндпоинт проверки входа
    /// </summary>
    /// <returns>Статус авторизации</returns>
    [Authorize]
    [HttpGet("CheckAuthorized")]
    [ProducesResponseType(typeof(AuthorizedDto),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<ActionResult<AuthorizedDto>> CheckAuthorized()
    {
        var (user, errorResponse) = await CheckAuth();
        if (errorResponse != null || user == null)
            return BadRequest(errorResponse ?? new Response("Error", "User not found. Try later."));

        return Ok(new AuthorizedDto(user.UserName!));
    }
}