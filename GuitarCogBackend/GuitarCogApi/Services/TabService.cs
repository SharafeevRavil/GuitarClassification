using GuitarCogApi.Dtos;
using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Tab;
using GuitarCogApi.Helpers;
using GuitarCogData;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

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
        var (file, response) = await _fileService.AddFileFromForm(addTabDto.File, 2);
        if (response != null || file == null)
            return (null, response);

        var tab = new Tab(file, addTabDto.Name, user, DateTimeOffset.UtcNow);
        _dbContext.Tabs.Add(tab);
        await _dbContext.SaveChangesAsync();
        return (tab, null);
    }

    public async Task<PagedResponse<TabListDto>> GetTabs(HttpRequest request, TabFilter tabFilter)
    {
        IQueryable<Tab> tabs = _dbContext.Tabs
            .Include(x => x.Author)
            .Include(x => x.TabFile);

        if (tabFilter.UserIds != null)
            tabs = tabs.Where(x => tabFilter.UserIds.Contains(x.Author.Id));

        var mapped = tabs
            .Select(x => new TabListDto(x.Id, x.Name, _fileService.GetUrlByFileId(request, x.TabFile.Id), 
                x.Author.Id, x.Author.UserName!, x.LoadDateTime));

        return await mapped.PagedResponse(tabFilter.Page ?? 1, tabFilter.PageSize ?? 10);
    }
}