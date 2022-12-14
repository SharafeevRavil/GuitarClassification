using GuitarCogApi.Dtos;
using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Tab;
using GuitarCogData;
using GuitarCogData.Models;

namespace GuitarCogApi.Services;

public class TabService
{
    private ApplicationDbContext _dbContext;
    private FileService _fileService;

    public TabService(ApplicationDbContext dbContext, FileService fileService)
    {
        _dbContext = dbContext;
        _fileService = fileService;
    }

    public async Task<(Tab?, Response?)> AddTab(AddTabDto addTabDto, User user)
    {
        var (file, response) = await _fileService.AddFileFromForm(addTabDto.File,2);
        if (response != null || file == null)
            return (null, response);

        var tab = new Tab(file, addTabDto.Name, user, DateTimeOffset.UtcNow);
        _dbContext.Tabs.Add(tab);
        await _dbContext.SaveChangesAsync();
        return (tab, null);
    }
}