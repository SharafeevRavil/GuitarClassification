namespace GuitarCogData.Models;

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

    public long Id { get; set; }
    
    public File TabFile { get; set; }
    
    public string Name { get; set; }
    public User Author { get; set; }
    public DateTimeOffset LoadDateTime { get; set; }
}