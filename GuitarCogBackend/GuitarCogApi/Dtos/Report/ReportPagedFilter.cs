using GuitarCogApi.Dtos.General;

namespace GuitarCogApi.Dtos.Report;

/// <summary>
/// Дто фильтра списка жалоб
/// </summary>
public class ReportPagedFilter : PagedFilter
{
    /// <summary>
    /// Показывать просмотренные модератором жалобы
    /// </summary>
    public bool ShowViewedReports { get; set; }
    /// <summary>
    /// Скрывать жалобы на забаненных пользователей
    /// </summary>
    public bool HideBannedUserTabsReports { get; set; }
}