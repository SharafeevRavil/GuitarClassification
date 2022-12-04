namespace GuitarCogApi.Dtos.Profile;

public class ChangeUsernameDto
{
    public ChangeUsernameDto(string newUsername)
    {
        NewUsername = newUsername;
    }

    public string NewUsername { get; set; }
}