namespace GuitarCogData.Models;

/// <summary>
/// Роль пользователя
/// </summary>
public enum Role
{
    /// <summary>
    /// Главный админ, может создавать модераторов
    /// </summary>
    SuperAdmin = 0,
    /// <summary>
    /// Модератор, реагирует на жалобы пользователей
    /// </summary>
    Moderator = 1,
}