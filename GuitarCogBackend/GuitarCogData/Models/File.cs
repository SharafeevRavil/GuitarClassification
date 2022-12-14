using System.ComponentModel.DataAnnotations.Schema;
using System.Diagnostics.CodeAnalysis;

namespace GuitarCogData.Models;

public class File
{
    public File(string fileName, byte[] bytes, string contentType)
    {
        Bytes = bytes;
        ContentType = contentType;
        FileName = fileName;
    }

    [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
    public Guid Id { get; set; }
    public string FileName { get; set; }
    public byte[] Bytes { get; set; }
    public string ContentType { get; set; }
}