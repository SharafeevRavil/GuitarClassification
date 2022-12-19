namespace GuitarCogApi.Dtos.Ad;

public class AdListDto
{
    public AdListDto(string url, int width, int height)
    {
        Url = url;
        Width = width;
        Height = height;
    }

    public string Url { get; set; }
    public int Width { get; set; }
    public int Height { get; set; }
}