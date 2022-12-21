using GuitarCogApi.Dtos.General;

namespace GuitarCogApi.Dtos.ModerUser;

/// <summary>
/// Дто фильтра в списке пользователей
/// </summary>
public class ModerUserPagedFilter : PagedFilter
{
    /// <summary>
    /// Скрывать забаненных пользователей
    /// </summary>
    public bool HideBannedUsers { get; set; } = false;
    /// <summary>
    /// Скрывать незабаненных пользователей
    /// </summary>
    public bool HideUnbannedUsers { get; set; } = false;
}