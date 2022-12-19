using GuitarCogApi.Dtos.General;

namespace GuitarCogApi.Dtos.Tab;

public class TabFilter : PagedFilter
{
    public string[]? UserIds { get; set; }
}