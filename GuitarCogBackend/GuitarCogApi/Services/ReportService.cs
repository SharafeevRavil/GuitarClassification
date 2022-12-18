using GuitarCogApi.Dtos.General;
using GuitarCogData;
using GuitarCogData.Models;
using Microsoft.EntityFrameworkCore;

namespace GuitarCogApi.Services;

public class ReportService
{
    private readonly ApplicationDbContext _dbContext;

    public ReportService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    public async Task<(Report?, Response?)> ReportTab(User user, long tabId)
    {
        if (await CheckReported(user.Id, tabId))
            return (null, new Response("Error", $"Tab {tabId} is already reported"));

        var tab = await _dbContext.Tabs.FindAsync(tabId);
        if (tab == null)
            return (null, new Response("Error", $"Tab {tabId} is not found"));

        var report = new Report(user, tab, DateTimeOffset.UtcNow);
        await _dbContext.Report.AddAsync(report);
        await _dbContext.SaveChangesAsync();
        
        return (report, null);
    }

    public Task<bool> CheckReported(string userId, long tabId) =>
        _dbContext.Report
            .Include(x => x.Tab)
            .Include(x => x.FromUser)
            .AnyAsync(x => x.FromUser.Id == userId && x.Tab.Id == tabId);
}