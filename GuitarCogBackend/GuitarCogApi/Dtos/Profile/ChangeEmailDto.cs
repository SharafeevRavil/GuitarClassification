namespace GuitarCogApi.Dtos.Profile;

public class ChangeEmailDto
{
    public ChangeEmailDto(string newEmail)
    {
        NewEmail = newEmail;
    }

    public string NewEmail { get; set; }
}