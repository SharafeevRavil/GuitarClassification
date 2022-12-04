using GuitarCogApi.Dtos.General;
using GuitarCogData;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Http.HttpResults;

namespace GuitarCogApi.Services;

public class ImageService
{
    private ApplicationDbContext _dbContext;

    public ImageService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    public string GetUrlByImageId(HttpRequest httpRequest, string imageId)
    {
        var baseUri = $"{httpRequest.Scheme}://{httpRequest.Host}";
        return $"{baseUri}/image/{imageId}";
    }

    public async Task<(Image?, Response?)> AddImageFromForm(IFormFile image)
    {
        using var memoryStream = new MemoryStream();
        await image.CopyToAsync(memoryStream);
        memoryStream.ToArray();

        if (memoryStream.Length > 2 * 1024 * 1024)
            return (null, new Response("Error", $"Image is too big. Upload an image less than 2 MB"));

        var img = new Image(image.FileName, memoryStream.ToArray(), image.ContentType);
        _dbContext.Images.Add(img);
        await _dbContext.SaveChangesAsync();
        return (img, null);
    }

    public async Task<Image?> LoadById(string imageId)
    {
        var img = _dbContext.Images.Find(imageId);
        return img;
    }
}