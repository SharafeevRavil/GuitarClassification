using Microsoft.AspNetCore.Identity;

namespace GuitarCogData.Models;

public class User : IdentityUser
{
    public string? RefreshToken { get; set; }
    public DateTimeOffset? RefreshTokenExpiryTime { get; set; }

    public File? AvatarImage { get; set; }

    public User? BannedBy { get; set; }
    public DateTimeOffset? BannedDate { get; set; }
    public bool IsBanned { get; set; }
}