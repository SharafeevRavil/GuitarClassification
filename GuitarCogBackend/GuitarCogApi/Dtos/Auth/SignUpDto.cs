namespace GuitarCogApi.Dtos.Auth;

public class SignUpDto
{
    public SignUpDto(string email, string username, string password)
    {
        Email = email;
        Username = username;
        Password = password;
    }

    public string Email { get; set; }
    public string Username { get; set; }
    public string Password { get; set; }
}