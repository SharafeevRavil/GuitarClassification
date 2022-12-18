namespace GuitarCogData.Models;

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

    public long Id { get; set; }
    public User FromUser { get; set; } = null!;
    public Tab Tab { get; set; } = null!;
    public DateTimeOffset ReportedDate { get; set; }
    public bool MarkedAsViewed { get; set; }
}