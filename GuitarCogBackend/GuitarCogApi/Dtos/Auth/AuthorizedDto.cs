namespace GuitarCogApi.Dtos.Auth;


public class AuthorizedDto
{
    public AuthorizedDto(string username)
    {
        Username = username;
    }

    public string Username { get; set; }
}