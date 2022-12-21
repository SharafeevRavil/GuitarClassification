namespace GuitarCogApi.Dtos.Auth;

/// <summary>
/// Дто токена
/// </summary>
public class TokenDto
{
    public TokenDto(string token, DateTime expiration, string refreshToken)
    {
        Token = token;
        Expiration = expiration;
        RefreshToken = refreshToken;
    }

    /// <summary>
    /// Токен
    /// </summary>
    public string Token { get; set; }
    /// <summary>
    /// Дата окончания токена
    /// </summary>
    public DateTime Expiration { get; set; }
    /// <summary>
    /// Рефреш токен
    /// </summary>
    public string RefreshToken { get; set; }
}