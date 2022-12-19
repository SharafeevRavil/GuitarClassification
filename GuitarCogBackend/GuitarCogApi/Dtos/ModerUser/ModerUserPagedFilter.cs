using GuitarCogApi.Dtos.General;

namespace GuitarCogApi.Dtos.ModerUser;

public class ModerUserPagedFilter : PagedFilter
{
    public bool HideBannedUsers { get; set; } = false;
    public bool HideUnbannedUsers { get; set; } = false;
}