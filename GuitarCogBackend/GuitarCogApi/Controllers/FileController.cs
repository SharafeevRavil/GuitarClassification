using System.Net;
using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Profile;
using GuitarCogApi.Services;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace GuitarCogApi.Controllers;

/// <summary>
/// Контроллер для скачивания файлов
/// </summary>
[ApiController]
[Route("[controller]")]
public class FileController : ControllerBase
{
    private readonly FileService _fileService;

    public FileController(FileService fileService)
    {
        _fileService = fileService;
    }
    /// <summary>
    /// Эндпоинт получения файла
    /// </summary>
    /// <param name="fileId">Id файла</param>
    /// <returns>Файл</returns>
    [HttpGet("{fileId:guid}")]
    [ProducesResponseType(typeof(FileStreamResult),StatusCodes.Status200OK)]
    [ProducesResponseType(typeof(Response),StatusCodes.Status400BadRequest)]
    public async Task<ActionResult> GetImage(Guid fileId)
    {
        var img = await _fileService.LoadById(fileId);
        if (img == null)
            return BadRequest(new Response("Error", $"Image not found"));
        return File(img.Bytes, img.ContentType, img.FileName);
    }
}