using Microsoft.AspNetCore.Identity;

namespace GuitarCogData.Models;

public class User : IdentityUser
{
    public string? RefreshToken { get; set; }
    public DateTimeOffset? RefreshTokenExpiryTime { get; set; }
    
    public string AvatarImageId { get; set; } 
}