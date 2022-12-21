namespace GuitarCogApi.Dtos.Tab;

/// <summary>
/// Дто ссылки на табулатуру
/// </summary>
public class AddTabRespDto
{
    public AddTabRespDto(string tabUrl)
    {
        TabUrl = tabUrl;
    }

    /// <summary>
    /// Ссылка
    /// </summary>
    public string TabUrl { get; set; }
}