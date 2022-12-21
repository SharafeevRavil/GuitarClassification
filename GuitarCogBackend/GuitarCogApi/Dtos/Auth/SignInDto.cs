namespace GuitarCogApi.Dtos.Auth;

/// <summary>
/// Дто входа
/// </summary>
public class SignInDto
{
    public SignInDto(string username, string password)
    {
        Username = username;
        Password = password;
    }

    /// <summary>
    /// Имя пользователя
    /// </summary>
    public string Username { get; set; }
    /// <summary>
    /// Пароль
    /// </summary>
    public string Password { get; set; }
}