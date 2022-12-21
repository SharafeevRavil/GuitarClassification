using GuitarCogApi.Dtos.Subscription;

namespace GuitarCogApi.Dtos.ModerUser;

/// <summary>
/// Дто модераторского профиля пользователя
/// </summary>
public class ModerUserDto
{
    public ModerUserDto(string id, string username, string email, string imageSrc, SubscriptionInfoDto subscription, IList<string> roles, bool isBanned)
    {
        Id = id;
        Username = username;
        Email = email;
        Subscription = subscription;
        ImageSrc = imageSrc;
        Roles = roles;
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
    /// Роли
    /// </summary>
    public IList<string> Roles { get; set; }
    /// <summary>
    /// Ссылка на аватар
    /// </summary>
    public string ImageSrc { get; set; }
    /// <summary>
    /// Информация о подписке
    /// </summary>
    public SubscriptionInfoDto Subscription { get; set; }
    /// <summary>
    /// Статус бана
    /// </summary>
    public bool IsBanned { get; set; }
}