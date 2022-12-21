using System.ComponentModel.DataAnnotations.Schema;
using System.Diagnostics.CodeAnalysis;

namespace GuitarCogData.Models;

/// <summary>
/// Модель файла
/// </summary>
public class File
{
    public File(string fileName, byte[] bytes, string contentType)
    {
        Bytes = bytes;
        ContentType = contentType;
        FileName = fileName;
    }

    /// <summary>
    /// Id
    /// </summary>
    [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
    public Guid Id { get; set; }
    /// <summary>
    /// Имя файла
    /// </summary>
    public string FileName { get; set; }
    /// <summary>
    /// Данные файла
    /// </summary>
    public byte[] Bytes { get; set; }
    /// <summary>
    /// Mimetype файла
    /// </summary>
    public string ContentType { get; set; }
}