namespace GuitarCogApi.Dtos.Auth;

public class ChangeUsernameDto
{
    public ChangeUsernameDto(string newUsername)
    {
        NewUsername = newUsername;
    }

    public string NewUsername { get; set; }
}