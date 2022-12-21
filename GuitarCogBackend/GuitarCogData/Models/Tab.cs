namespace GuitarCogData.Models;

/// <summary>
/// Табулатура
/// </summary>
public class Tab
{
    public Tab(File tabFile, string name, User author, DateTimeOffset loadDateTime)
    {
        Name = name;
        Author = author;
        LoadDateTime = loadDateTime;
        TabFile = tabFile;
    }

    public Tab()
    {
        
    }

    /// <summary>
    /// Id
    /// </summary>
    public long Id { get; set; }
    /// <summary>
    /// Файл табулатуры
    /// </summary>
    public File TabFile { get; set; }
    /// <summary>
    /// Название табулатуры
    /// </summary>
    public string Name { get; set; }
    /// <summary>
    /// Создатель табулатуры
    /// </summary>
    public User Author { get; set; }
    /// <summary>
    /// Дата загрузки на сервер
    /// </summary>
    public DateTimeOffset LoadDateTime { get; set; }
}