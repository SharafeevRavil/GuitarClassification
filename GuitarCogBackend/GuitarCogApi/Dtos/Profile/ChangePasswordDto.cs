namespace GuitarCogApi.Dtos.Profile;

public class ChangePasswordDto
{
    public ChangePasswordDto(string oldPassword, string newPassword)
    {
        OldPassword = oldPassword;
        NewPassword = newPassword;
    }

    public string OldPassword { get; set; }
    public string NewPassword { get; set; }
}