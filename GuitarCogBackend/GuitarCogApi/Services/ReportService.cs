﻿using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Report;
using GuitarCogApi.Helpers;
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
            return (null, new Response("Error", $"Tab {tabId} is already reported."));

        var tab = await _dbContext.Tabs.Include(x => x.Author)
            .FirstOrDefaultAsync(x => x.Id == tabId);
        if (tab == null)
            return (null, new Response("Error", $"Tab {tabId} is not found."));
        if (tab.Author.Id == user.Id)
            return (null, new Response("Error", $"Cannot report {tabId} tab, because it belongs to you."));

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

    public async Task<PagedResponse<ReportListDto>> GetReports(ReportPagedFilter filter)
    {
        IQueryable<Report> reports = _dbContext.Report
            .Include(x => x.Tab)
            .ThenInclude(x => x.Author)
            .Include(x => x.FromUser)
            .OrderBy(x => x.MarkedAsViewed)
            .ThenBy(x => x.ReportedDate);

        if (!filter.ShowViewedReports) 
            reports = reports.Where(x => !x.MarkedAsViewed);

        return await reports
            .Select(x => new ReportListDto(x.Id, x.FromUser.Id, x.FromUser.UserName!, x.Tab.Id, x.Tab.Author.Id,
                x.MarkedAsViewed, x.ReportedDate))
            .PagedResponse(filter.Page ?? 1, filter.PageSize ?? 10);
    }

    public async Task<Response?> MarkAsViewed(long reportId)
    {
        var report = await _dbContext.Report.FirstOrDefaultAsync(x => x.Id == reportId);
        if (report == null)
            return new Response("Error", $"Report {reportId} is not found");

        report.MarkedAsViewed = true;
        await _dbContext.SaveChangesAsync();
        return null;
    }
}