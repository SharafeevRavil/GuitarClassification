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

    public string GetUrlByFileId(HttpRequest httpRequest, Guid imageId) => httpRequest.UriWithBase($"/file/{imageId}");

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

    public async Task<File?> LoadById(Guid imageId)
    {
        var file = await _dbContext.Files.FindAsync(imageId);
        return file;
    }
}