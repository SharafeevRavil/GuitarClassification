namespace GuitarCogApi.Dtos.Profile;

/// <summary>
/// Дто смены почты
/// </summary>
public class ChangeEmailDto
{
    public ChangeEmailDto(string newEmail)
    {
        NewEmail = newEmail;
    }

    /// <summary>
    /// Новая почта
    /// </summary>
    public string NewEmail { get; set; }
}