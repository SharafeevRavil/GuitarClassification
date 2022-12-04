namespace GuitarCogData.Models;

public class Image
{
    public Image(string fileName, byte[] bytes, string contentType)
    {
        Id = Guid.NewGuid().ToString();
        Bytes = bytes;
        ContentType = contentType;
        FileName = fileName;
    }

    public string Id { get; set; }
    public string FileName { get; set; }
    public byte[] Bytes { get; set; }
    public string ContentType { get; set; }
}