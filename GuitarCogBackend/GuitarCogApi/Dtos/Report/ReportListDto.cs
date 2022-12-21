namespace GuitarCogApi.Dtos.Report;

/// <summary>
/// Дто жалобы из списка
/// </summary>
public class ReportListDto
{
    public ReportListDto(long id, 
        string fromUserId, string fromUserName, 
        long tabId, string tabName, string tabUrl,
        string reportedUserId, string reportedUserName, 
        bool isReportMarkedAsViewed, DateTimeOffset reportedDate)
    {
        Id = id;
        
        FromUserId = fromUserId;
        FromUserName = fromUserName;
        
        TabId = tabId;
        TabName = tabName;
        TabUrl = tabUrl;
        
        ReportedUserId = reportedUserId;
        IsReportMarkedAsViewed = isReportMarkedAsViewed;
        
        ReportedDate = reportedDate;
        ReportedUserName = reportedUserName;
    }

    public ReportListDto()
    {
    }

    /// <summary>
    /// Id
    /// </summary>
    public long Id { get; set; }
    /// <summary>
    /// Id отправителя жалобы
    /// </summary>
    public string FromUserId { get; set; }
    /// <summary>
    /// Имя пользователя отправителя жалобы
    /// </summary>
    public string FromUserName { get; set; }
    /// <summary>
    /// Id табулатуры
    /// </summary>
    public long TabId { get; set; }
    /// <summary>
    /// Название табулатуры
    /// </summary>
    public string TabName { get; set; }
    /// <summary>
    /// Ссылка на табулатуру
    /// </summary>
    public string TabUrl { get; set; }
    /// <summary>
    /// Id пользователя под жалобой
    /// </summary>
    public string ReportedUserId { get; set; }
    /// <summary>
    /// Имя пользователя пользователя под жалобой
    /// </summary>
    public string ReportedUserName { get; set; }
    /// <summary>
    /// Просмотрена ли жалоба модератором
    /// </summary>
    public bool IsReportMarkedAsViewed { get; set; }
    /// <summary>
    /// Дата отправки жалобы
    /// </summary>
    public DateTimeOffset ReportedDate { get; set; }
}