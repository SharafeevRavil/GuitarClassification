namespace GuitarCogApi.Dtos.Ad;
/// <summary>
/// Дто релкамного баннера
/// </summary>
public class AdListDto
{
    public AdListDto(string url, int width, int height)
    {
        Url = url;
        Width = width;
        Height = height;
    }

    /// <summary>
    /// Ссылка на баннер
    /// </summary>
    public string Url { get; set; }
    /// <summary>
    /// Ширина баннера
    /// </summary>
    public int Width { get; set; }
    /// <summary>
    /// Высота баннера
    /// </summary>
    public int Height { get; set; }
}