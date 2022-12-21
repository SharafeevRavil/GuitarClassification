namespace GuitarCogApi.Dtos.ModerUser;

/// <summary>
/// Дто пользователя из списка
/// </summary>
public class ModerUserListDto
{
    public ModerUserListDto(string id, string username, string email, bool isBanned)
    {
        Id = id;
        Username = username;
        Email = email;
        IsBanned = isBanned;
    }

    /// <summary>
    /// Id
    /// </summary>
    public string Id { get; set; }
    /// <summary>
    /// Имя пользователя
    /// </summary>
    public string Username { get; set; }
    /// <summary>
    /// Почта
    /// </summary>
    public string Email { get; set; }
    /// <summary>
    /// Статус бана
    /// </summary>
    public bool IsBanned { get; set; }
}