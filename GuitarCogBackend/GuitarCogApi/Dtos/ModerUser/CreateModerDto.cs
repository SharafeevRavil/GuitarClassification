namespace GuitarCogApi.Dtos.ModerUser;

/// <summary>
/// Дто создания модератора
/// </summary>
public class CreateModerDto
{
    public CreateModerDto(string username, string email, string password)
    {
        Username = username;
        Email = email;
        Password = password;
    }

    public CreateModerDto()
    {
        
    }

    /// <summary>
    /// Имя пользователя
    /// </summary>
    public string Username { get; set; } = null!;
    /// <summary>
    /// Почта
    /// </summary>
    public string Email { get; set; } = null!;
    /// <summary>
    /// Пароль
    /// </summary>
    public string Password { get; set; } = null!;
}