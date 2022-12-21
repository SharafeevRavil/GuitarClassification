namespace GuitarCogApi.Dtos.Auth;

/// <summary>
/// Дто обновления токена
/// </summary>
public class TokenPairDto
{
    public TokenPairDto(string accessToken, string refreshToken)
    {
        AccessToken = accessToken;
        RefreshToken = refreshToken;
    }

    /// <summary>
    /// Токен
    /// </summary>
    public string AccessToken { get; set; }
    /// <summary>
    /// Рефреш токен
    /// </summary>
    public string RefreshToken { get; set; }
}