using GuitarCogApi.Dtos.General;

namespace GuitarCogApi.Dtos.Report;

public class ReportPagedFilter : PagedFilter
{
    public bool ShowViewedReports { get; set; }
    public bool HideBannedUserTabsReports { get; set; }
}