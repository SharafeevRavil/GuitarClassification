namespace GuitarCogApi.Dtos.Auth;

public class TokenDto
{
    public TokenDto(string token, DateTime expiration, string refreshToken)
    {
        Token = token;
        Expiration = expiration;
        RefreshToken = refreshToken;
    }

    public string Token { get; set; }
    public DateTime Expiration { get; set; }
    public string RefreshToken { get; set; }
}