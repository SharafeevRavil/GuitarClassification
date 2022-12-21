namespace GuitarCogApi.Dtos.General;

/// <summary>
/// Дто фильтра для пагинации (база)
/// </summary>
public class PagedFilter
{
    /// <summary>
    /// Страница
    /// </summary>
    public int? Page { get; set; } = 1;
    /// <summary>
    /// Размер страницы
    /// </summary>
    public int? PageSize { get; set; } = 10;
}