namespace GuitarCogApi.Dtos.Tab;

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

    public string Name { get; set; }
    public IFormFile File { get; set; }
}