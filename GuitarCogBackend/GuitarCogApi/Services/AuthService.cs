using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Security.Cryptography;
using System.Text;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Identity;
using Microsoft.IdentityModel.Tokens;

namespace GuitarCogApi.Services;

public class AuthService
{
    private readonly IConfiguration _configuration;
    private readonly UserManager<User> _userManager;

    public AuthService(IConfiguration configuration, UserManager<User> userManager)
    {
        _configuration = configuration;
        _userManager = userManager;
    }

    /// <summary>
    /// Генерация токенов
    /// </summary>
    /// <param name="user"></param>
    /// <returns></returns>
    public async Task<(JwtSecurityToken token, string refreshToken)> GenerateTokensPair(User user)
    {
        var token = await GetToken(user);
        var refreshToken = GenerateRefreshToken();

        int.TryParse(_configuration["JWT:RefreshTokenExpiresInDays"], out var refreshTokenValidityInDays);
        user.RefreshToken = refreshToken;
        user.RefreshTokenExpiryTime = DateTimeOffset.UtcNow.AddDays(refreshTokenValidityInDays);
        await _userManager.UpdateAsync(user);
        return (token, refreshToken);
    }

    /// <summary>
    /// Генерация токенов для пользователя
    /// </summary>
    /// <param name="user"></param>
    /// <returns></returns>
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

        var token = new JwtSecurityToken(_configuration["JWT:ValidIssuer"], _configuration["JWT:ValidAudience"],
            expires: DateTime.Now.AddMinutes(expiresInMinutes),
            claims: authClaims,
            signingCredentials: new SigningCredentials(authSigningKey, SecurityAlgorithms.HmacSha256)
        );

        return token;
    }

    /// <summary>
    /// Генерация refresh токена
    /// </summary>
    /// <returns></returns>
    private static string GenerateRefreshToken()
    {
        var randomNumber = new byte[64];
        using var rng = RandomNumberGenerator.Create();
        rng.GetBytes(randomNumber);
        return Convert.ToBase64String(randomNumber);
    }

    /// <summary>
    /// Получение информации из просроченного токена
    /// </summary>
    /// <param name="token"></param>
    /// <returns></returns>
    /// <exception cref="SecurityTokenException"></exception>
    public ClaimsPrincipal? GetPrincipalFromExpiredToken(string? token)
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