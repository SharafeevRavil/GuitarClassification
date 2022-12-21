using GuitarCogApi.Dtos.General;

namespace GuitarCogApi.Dtos.Tab;

/// <summary>
/// Дто фильтра списка табулатур
/// </summary>
public class TabFilter : PagedFilter
{
    /// <summary>
    /// Пользователи, табулатуры которых надо получить
    /// </summary>
    public string[]? UserIds { get; set; }
}