namespace GuitarCogApi.Dtos.Profile;

/// <summary>
/// Дто аватара
/// </summary>
public class AvatarDto
{
    public AvatarDto(string avatarUrl)
    {
        AvatarUrl = avatarUrl;
    }

    /// <summary>
    /// Ссылка
    /// </summary>
    public string AvatarUrl { get; set; }
}