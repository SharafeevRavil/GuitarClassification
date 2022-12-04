using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Profile;
using GuitarCogApi.Services;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace GuitarCogApi.Controllers;

[ApiController]
[Route("[controller]")]
public class ImageController : ControllerBase
{
    private readonly ImageService _imageService;

    public ImageController(ImageService imageService)
    {
        _imageService = imageService;
    }

    [HttpGet("{imageId}")]
    public async Task<IActionResult> GetImage(string imageId)
    {
        var img = await _imageService.LoadById(imageId);
        if (img == null)
            return BadRequest(new Response("Error", $"Image not found"));
        return File(img.Bytes, img.ContentType, img.FileName);
    }
}