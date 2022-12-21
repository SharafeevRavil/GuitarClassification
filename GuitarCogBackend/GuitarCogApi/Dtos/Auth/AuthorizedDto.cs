namespace GuitarCogApi.Dtos.Auth;

/// <summary>
/// Дто проверки авторизации
/// </summary>
public class AuthorizedDto
{
    public AuthorizedDto(string username)
    {
        Username = username;
    }

    /// <summary>
    /// Имя текущего пользователя
    /// </summary>
    public string Username { get; set; }
}