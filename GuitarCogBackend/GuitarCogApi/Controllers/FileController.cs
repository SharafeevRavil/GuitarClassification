using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Profile;
using GuitarCogApi.Services;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace GuitarCogApi.Controllers;

[ApiController]
[Route("[controller]")]
public class FileController : ControllerBase
{
    private readonly FileService _fileService;

    public FileController(FileService fileService)
    {
        _fileService = fileService;
    }

    [HttpGet("{imageId}")]
    public async Task<IActionResult> GetImage(Guid imageId)
    {
        var img = await _fileService.LoadById(imageId);
        if (img == null)
            return BadRequest(new Response("Error", $"Image not found"));
        return File(img.Bytes, img.ContentType, img.FileName);
    }
}