namespace GuitarCogApi.Dtos.Profile;

/// <summary>
/// Дто смены имени пользователя
/// </summary>
public class ChangeUsernameDto
{
    public ChangeUsernameDto(string newUsername)
    {
        NewUsername = newUsername;
    }

    /// <summary>
    /// Новое имя пользователя
    /// </summary>
    public string NewUsername { get; set; }
}