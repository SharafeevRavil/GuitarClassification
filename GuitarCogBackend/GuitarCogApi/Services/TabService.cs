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
    private readonly ApplicationDbContext _dbContext;
    private readonly SubscriptionService _subscriptionService;
    private readonly FileService _fileService;
    private readonly ReportService _reportService;

    public TabService(ApplicationDbContext dbContext, SubscriptionService subscriptionService, FileService fileService, ReportService reportService)
    {
        _dbContext = dbContext;
        _fileService = fileService;
        _reportService = reportService;
        _subscriptionService = subscriptionService;
    }

    public async Task<(Tab?, Response?)> AddTab(AddTabDto addTabDto, User user)
    {
        var limits = await GetTabLimit(user);
        if (limits.TabCount >= limits.TabLimit)
            return (null, new Response("Error", $"User tabs limit exceeded - {limits.TabCount} of {limits.TabLimit}"));
            
        var (file, response) = await _fileService.AddFileFromForm(addTabDto.File, 2);
        if (response != null || file == null)
            return (null, response);

        var tab = new Tab(file, addTabDto.Name, user, DateTimeOffset.UtcNow);
        _dbContext.Tabs.Add(tab);
        await _dbContext.SaveChangesAsync();
        return (tab, null);
    }

    public async Task<PagedResponse<TabListDto>> GetTabs(HttpRequest request, TabFilter tabFilter, User? user = null)
    {
        IQueryable<Tab> tabs = _dbContext.Tabs
            .Include(x => x.Author)
            .Include(x => x.TabFile);

        if (tabFilter.UserIds != null)
            tabs = tabs.Where(x => tabFilter.UserIds.Contains(x.Author.Id));

        
        var mapped = tabs.Select(x => new TabListDto(x.Id, x.Name, _fileService.GetUrlByFileId(request, x.TabFile.Id), 
                x.Author.Id, x.Author.UserName!, x.LoadDateTime));

        var paged = await mapped.PagedResponse(tabFilter.Page ?? 1, tabFilter.PageSize ?? 10);

        if (user == null) return paged;
        
        foreach (var tabListDto in paged.Data)
            tabListDto.IsReported = await _reportService.CheckReported(user.Id, tabListDto.Id);
        return paged;
    }

    public async Task<TabLimitDto> GetTabLimit(User user)
    {
        const int userLimit = 1;
        const int subLimit = 100;

        var userSubscribed = (await _subscriptionService.CheckSubscribed(user)).IsSubscribed;
        var limit = userSubscribed ? subLimit : userLimit;
        
        var currentTabs = await _dbContext.Tabs
            .Include(x => x.Author)
            .CountAsync(x => x.Author.Id == user.Id);
        return new TabLimitDto(currentTabs, limit);
    }
}