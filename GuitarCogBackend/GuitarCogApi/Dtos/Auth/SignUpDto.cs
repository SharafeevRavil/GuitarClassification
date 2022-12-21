namespace GuitarCogApi.Dtos.Auth;

/// <summary>
/// Дто регистрации
/// </summary>
public class SignUpDto
{
    public SignUpDto(string email, string username, string password)
    {
        Email = email;
        Username = username;
        Password = password;
    }

    /// <summary>
    /// Почта
    /// </summary>
    public string Email { get; set; }
    /// <summary>
    /// Имя пользователя
    /// </summary>
    public string Username { get; set; }
    /// <summary>
    /// Пароль
    /// </summary>
    public string Password { get; set; }
}