using GuitarCogApi.Dtos.General;
using GuitarCogApi.Helpers;
using GuitarCogData;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Http.HttpResults;
using File = GuitarCogData.Models.File;

namespace GuitarCogApi.Services;

public class FileService
{
    private ApplicationDbContext _dbContext;

    public FileService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    /// <summary>
    /// Получение ссылки на файл по его Id
    /// </summary>
    /// <param name="httpRequest">HttpRequest текущего контекста</param>
    /// <param name="imageId">Id файла</param>
    /// <returns>Ссылка на файл</returns>
    public string GetUrlByFileId(HttpRequest httpRequest, Guid imageId) => httpRequest.UriWithBase($"/file/{imageId}");

    /// <summary>
    /// Добавление файла
    /// </summary>
    /// <param name="form">Форма файла</param>
    /// <param name="limitInMb">Лимит файла в МБ</param>
    /// <returns>Файл/ошибка</returns>
    public async Task<(File?, Response?)> AddFileFromForm(IFormFile form, int limitInMb)
    {
        using var memoryStream = new MemoryStream();
        await form.CopyToAsync(memoryStream);
        memoryStream.ToArray();

        if (memoryStream.Length > limitInMb * 1024 * 1024)
            return (null, new Response("Error", $"File is too big. Upload an image less than {limitInMb} MB"));

        var file = new File(form.FileName, memoryStream.ToArray(), form.ContentType);
        _dbContext.Files.Add(file);
        await _dbContext.SaveChangesAsync();
        return (file, null);
    }

    /// <summary>
    /// Получение файла по Id
    /// </summary>
    /// <param name="imageId">Id файла</param>
    /// <returns>Файл</returns>
    public async Task<File?> LoadById(Guid imageId)
    {
        var file = await _dbContext.Files.FindAsync(imageId);
        return file;
    }
}