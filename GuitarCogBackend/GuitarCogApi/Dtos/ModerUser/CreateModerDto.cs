namespace GuitarCogApi.Dtos.Moder.ModerUser;

public class CreateModerDto
{
    public CreateModerDto(string username, string email, string password)
    {
        Username = username;
        Email = email;
        Password = password;
    }

    public CreateModerDto()
    {
        
    }

    public string Username { get; set; } = null!;
    public string Email { get; set; } = null!;
    public string Password { get; set; } = null!;
}