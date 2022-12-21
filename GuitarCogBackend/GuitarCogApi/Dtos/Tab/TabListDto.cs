namespace GuitarCogApi.Dtos.Tab;

/// <summary>
/// Дто табулатуры из списка
/// </summary>
public class TabListDto
{
    public TabListDto(long id, string name, string fileUrl, string authorId, string authorName, DateTimeOffset loadDateTime)
    {
        Id = id;
        Name = name;
        AuthorId = authorId;
        LoadDateTime = loadDateTime;
        AuthorName = authorName;
        FileUrl = fileUrl;
    }

    /// <summary>
    /// Id
    /// </summary>
    public long Id { get; set; }
    /// <summary>
    /// Название табулатуры
    /// </summary>
    public string Name { get; set; }
    /// <summary>
    /// Ссылка на файл
    /// </summary>
    public string FileUrl { get; set; }
    /// <summary>
    /// Id автора
    /// </summary>
    public string AuthorId { get; set; }
    /// <summary>
    /// Имя пользователя автора
    /// </summary>
    public string AuthorName { get; set; }
    /// <summary>
    /// Дата загрузки табулатуры
    /// </summary>
    public DateTimeOffset LoadDateTime { get; set; }
    /// <summary>
    /// Зарепорчена ли табулатура текущим пользователем
    /// </summary>
    public bool IsReported { get; set; }
}