namespace GuitarCogApi.Dtos.Profile;

/// <summary>
/// Дто профиля пользователя
/// </summary>
public class ProfileDto
{
    public ProfileDto(string id, string username, string email, string imageUrl)
    {
        Id = id;
        Username = username;
        Email = email;
        ImageUrl = imageUrl;
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
    /// Ссылка на аватарку
    /// </summary>
    public string ImageUrl { get; set; }
}