namespace GuitarCogApi.Dtos.Tab;

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

    public long Id { get; set; }
    public string Name { get; set; }
    public string FileUrl { get; set; }
    public string AuthorId { get; set; }
    public string AuthorName { get; set; }
    public DateTimeOffset LoadDateTime { get; set; }
    public bool IsReported { get; set; }
}