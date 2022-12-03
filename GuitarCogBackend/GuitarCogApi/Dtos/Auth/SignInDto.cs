namespace GuitarCogApi.Dtos.Auth;

public class SignInDto
{
    public SignInDto(string username, string password)
    {
        Username = username;
        Password = password;
    }

    public string Username { get; set; }
    public string Password { get; set; }
}