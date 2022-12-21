namespace GuitarCogData.Models;

/// <summary>
/// Жалоба на табулатуру
/// </summary>
public class Report
{
    public Report(User fromUser, Tab tab, DateTimeOffset reportedDate)
    {
        FromUser = fromUser;
        Tab = tab;
        ReportedDate = reportedDate;
    }

    public Report()
    {
        
    }

    /// <summary>
    /// Id
    /// </summary>
    public long Id { get; set; }
    /// <summary>
    /// Юзер, отправивший жалобу
    /// </summary>
    public User FromUser { get; set; } = null!;
    /// <summary>
    /// Табулатуа, на которую пожаловались
    /// </summary>
    public Tab Tab { get; set; } = null!;
    /// <summary>
    /// Дата отправки жалобы
    /// </summary>
    public DateTimeOffset ReportedDate { get; set; }
    /// <summary>
    /// Проверена ли жалоба модератором
    /// </summary>
    public bool MarkedAsViewed { get; set; }
}