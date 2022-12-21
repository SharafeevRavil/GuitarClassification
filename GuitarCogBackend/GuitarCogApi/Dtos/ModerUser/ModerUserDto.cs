using GuitarCogApi.Dtos.Subscription;

namespace GuitarCogApi.Dtos.ModerUser;

public class ModerUserDto
{
    public ModerUserDto(string id, string username, string email, string imageSrc, SubscriptionInfoDto subscription, IList<string> roles, bool isBanned)
    {
        Id = id;
        Username = username;
        Email = email;
        Subscription = subscription;
        ImageSrc = imageSrc;
        Roles = roles;
        IsBanned = isBanned;
    }

    public string Id { get; set; }
    public string Username { get; set; }
    public string Email { get; set; }
    public IList<string> Roles { get; set; }
    public string ImageSrc { get; set; }
    public SubscriptionInfoDto Subscription { get; set; }
    public bool IsBanned { get; set; }
}