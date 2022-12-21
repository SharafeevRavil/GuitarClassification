using Microsoft.AspNetCore.Identity;

namespace GuitarCogData.Models;

/// <summary>
/// Пользователь
/// </summary>
public class User : IdentityUser
{
    /// <summary>
    /// Refresh token
    /// </summary>
    public string? RefreshToken { get; set; }
    /// <summary>
    /// Время истечения refresh token'а
    /// </summary>
    public DateTimeOffset? RefreshTokenExpiryTime { get; set; }
    /// <summary>
    /// Файл аватара
    /// </summary>
    public File? AvatarImage { get; set; }
    /// <summary>
    /// Кем забанен
    /// </summary>
    public User? BannedBy { get; set; }
    /// <summary>
    /// Время бана
    /// </summary>
    public DateTimeOffset? BannedDate { get; set; }
    /// <summary>
    /// Статус бана
    /// </summary>
    public bool IsBanned { get; set; }
}