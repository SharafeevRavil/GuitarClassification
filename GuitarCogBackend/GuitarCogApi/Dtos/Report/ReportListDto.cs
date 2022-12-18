namespace GuitarCogApi.Dtos.Report;

public class ReportListDto
{
    public ReportListDto(long id, string fromUserId, string fromUserName, long tabId, string reportedUserId,
        string reportedUserName, bool isReportMarkedAsViewed, DateTimeOffset reportedDate)
    {
        Id = id;
        FromUserId = fromUserId;
        FromUserName = fromUserName;
        TabId = tabId;
        ReportedUserId = reportedUserId;
        IsReportMarkedAsViewed = isReportMarkedAsViewed;
        ReportedDate = reportedDate;
        ReportedUserName = reportedUserName;
    }

    public ReportListDto()
    {
    }

    public long Id { get; set; }
    public string FromUserId { get; set; }
    public string FromUserName { get; set; }
    public long TabId { get; set; }
    public string ReportedUserId { get; set; }
    public string ReportedUserName { get; set; }
    public bool IsReportMarkedAsViewed { get; set; }
    public DateTimeOffset ReportedDate { get; set; }
}