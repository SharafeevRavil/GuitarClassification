namespace GuitarCogApi.Dtos.General;

/// <summary>
/// Дто пагинации
/// </summary>
/// <typeparam name="T"></typeparam>
public class PagedResponse<T>
{
    public PagedResponse(List<T> data, int page, int pageCount, int elementsCount)
    {
        Data = data;
        Page = page;
        PageCount = pageCount;
        ElementsCount = elementsCount;
    }
    /// <summary>
    /// Страница
    /// </summary>
    public int Page { get; set; }
    /// <summary>
    /// Число элементов на странице
    /// </summary>
    public int PageCount { get; set; }
    /// <summary>
    /// Всего элементов
    /// </summary>
    public int ElementsCount { get; set; }
    /// <summary>
    /// Пагинированные данные
    /// </summary>
    public List<T> Data { get; set; }
}