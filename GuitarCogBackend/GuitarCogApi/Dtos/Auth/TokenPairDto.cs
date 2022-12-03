namespace GuitarCogApi.Dtos.Auth;

public class TokenPairDto
{
    public TokenPairDto(string accessToken, string refreshToken)
    {
        AccessToken = accessToken;
        RefreshToken = refreshToken;
    }

    public string AccessToken { get; set; }
    public string RefreshToken { get; set; }
}