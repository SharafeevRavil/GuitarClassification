namespace GuitarCogApi.Dtos.Tab;

public class AddTabRespDto
{
    public AddTabRespDto(string tabUrl)
    {
        TabUrl = tabUrl;
    }

    public string TabUrl { get; set; }
}