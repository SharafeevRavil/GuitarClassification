namespace GuitarCogApi.Dtos.Tab;

public class TabListDto
{
    public TabListDto()
    {
    }

    public TabListDto(long id, string name, string authorId, DateTimeOffset loadDateTime)
    {
        Id = id;
        Name = name;
        AuthorId = authorId;
        LoadDateTime = loadDateTime;
    }

    public long Id { get; set; }
    public string Name { get; set; }
    public string AuthorId { get; set; }
    public DateTimeOffset LoadDateTime { get; set; }
}