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
    private readonly RoleManager<IdentityRole> _roleManager;
    private readonly IConfiguration _configuration;

    public AuthController(UserManager<User> userManager, RoleManager<IdentityRole> roleManager,
        IConfiguration configuration)
    {
        _userManager = userManager;
        _roleManager = roleManager;
        _configuration = configuration;
    }

    [HttpPost("SignIn")]
    public async Task<IActionResult> SignIn([FromBody] SignInDto model)
    {
        var user = await _userManager.FindByNameAsync(model.Username);
        if (user == null || !await _userManager.CheckPasswordAsync(user, model.Password)) return Unauthorized();

        var (token, refreshToken) = await GenerateTokensPair(user);

        return Ok(new TokenDto(new JwtSecurityTokenHandler().WriteToken(token), token.ValidTo, refreshToken));
    }

    [HttpPost("SignUp")]
    public async Task<IActionResult> SignUp([FromBody] SignUpDto model)
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

        var (token, refreshToken) = await GenerateTokensPair(user);

        return Ok(new TokenDto(new JwtSecurityTokenHandler().WriteToken(token), token.ValidTo, refreshToken));
    }

    [HttpPost("RefreshToken")]
    public async Task<IActionResult> RefreshToken([FromBody] TokenPairDto tokenModel)
    {
        var accessToken = tokenModel.AccessToken;
        var refreshToken = tokenModel.RefreshToken;

        var principal = GetPrincipalFromExpiredToken(accessToken);
        if (principal == null)
        {
            return BadRequest(new Response("Error", "Invalid access token or refresh token"));
        }

        var username = principal.Identity!.Name;
        var user = await _userManager.FindByNameAsync(username!);

        if (user == null || user.RefreshToken != refreshToken || user.RefreshTokenExpiryTime <= DateTimeOffset.UtcNow)
        {
            return BadRequest(new Response("Error", "Invalid access token or refresh token"));
        }

        var (newToken, newRefreshToken) = await GenerateTokensPair(user);
        return Ok(new TokenDto(new JwtSecurityTokenHandler().WriteToken(newToken), newToken.ValidTo, newRefreshToken));
    }

    [Authorize]
    [HttpPost("CheckAuthorized")]
    public async Task<IActionResult> CheckAuthorized()
    {
        var username = User.Identity!.Name;
        return Ok(new { Username = username });
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

        var (token, refreshToken) = await GenerateTokensPair(user);
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

        return Ok();
    }

    private async Task<(JwtSecurityToken token, string refreshToken)> GenerateTokensPair(User user)
    {
        var token = await GetToken(user);
        var refreshToken = GenerateRefreshToken();

        int.TryParse(_configuration["JWT:RefreshTokenExpiresInDays"], out var refreshTokenValidityInDays);
        user.RefreshToken = refreshToken;
        user.RefreshTokenExpiryTime = DateTimeOffset.UtcNow.AddDays(refreshTokenValidityInDays);
        await _userManager.UpdateAsync(user);
        return (token, refreshToken);
    }

    private async Task<JwtSecurityToken> GetToken(User user)
    {
        var userRoles = await _userManager.GetRolesAsync(user);

        var authClaims = new List<Claim>
        {
            new(ClaimTypes.Name, user.UserName!),
            new(ClaimTypes.NameIdentifier, user.Id),
            new(JwtRegisteredClaimNames.Jti, Guid.NewGuid().ToString()),
        };

        authClaims.AddRange(userRoles.Select(userRole => new Claim(ClaimTypes.Role, userRole)));
        //

        var authSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_configuration["JWT:Secret"]!));
        _ = int.TryParse(_configuration["JWT:ExpiresInMinutes"], out var expiresInMinutes);

        var token = new JwtSecurityToken(
            _configuration["JWT:ValidIssuer"],
            _configuration["JWT:ValidAudience"],
            expires: DateTime.Now.AddMinutes(expiresInMinutes),
            claims: authClaims,
            signingCredentials: new SigningCredentials(authSigningKey, SecurityAlgorithms.HmacSha256)
        );

        return token;
    }

    private static string GenerateRefreshToken()
    {
        var randomNumber = new byte[64];
        using var rng = RandomNumberGenerator.Create();
        rng.GetBytes(randomNumber);
        return Convert.ToBase64String(randomNumber);
    }

    private ClaimsPrincipal? GetPrincipalFromExpiredToken(string? token)
    {
        var tokenValidationParameters = new TokenValidationParameters
        {
            ValidateAudience = false,
            ValidateIssuer = false,
            ValidateIssuerSigningKey = true,
            IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_configuration["JWT:Secret"]!)),
            ValidateLifetime = false
        };

        var tokenHandler = new JwtSecurityTokenHandler();
        var principal = tokenHandler.ValidateToken(token, tokenValidationParameters, out var securityToken);
        if (securityToken is not JwtSecurityToken jwtSecurityToken ||
            !jwtSecurityToken.Header.Alg.Equals(SecurityAlgorithms.HmacSha256,
                StringComparison.InvariantCultureIgnoreCase))
            throw new SecurityTokenException("Invalid token");

        return principal;
    }
}