namespace GuitarCogApi.Dtos.Profile;

/// <summary>
/// Дто смены пароля
/// </summary>
public class ChangePasswordDto
{
    public ChangePasswordDto(string oldPassword, string newPassword)
    {
        OldPassword = oldPassword;
        NewPassword = newPassword;
    }

    /// <summary>
    /// Старый пароль
    /// </summary>
    public string OldPassword { get; set; }
    /// <summary>
    /// Новый пароль
    /// </summary>
    public string NewPassword { get; set; }
}