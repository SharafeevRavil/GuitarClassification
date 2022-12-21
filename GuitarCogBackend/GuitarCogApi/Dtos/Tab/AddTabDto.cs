namespace GuitarCogApi.Dtos.Tab;

/// <summary>
/// Дто добавления табулатуры
/// </summary>
public class AddTabDto
{
    public AddTabDto(string name, IFormFile file)
    {
        Name = name;
        File = file;
    }

    public AddTabDto()
    {
        
    }

    /// <summary>
    /// Название табулатуры
    /// </summary>
    public string Name { get; set; } = null!;
    /// <summary>
    /// Файл табулатуры
    /// </summary>
    public IFormFile File { get; set; } = null!;
}