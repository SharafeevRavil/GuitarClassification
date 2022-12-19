namespace GuitarCogApi.Dtos.ModerUser;

public class ModerUserListDto
{
    public ModerUserListDto(string id, string username, string email, bool isBanned)
    {
        Id = id;
        Username = username;
        Email = email;
        IsBanned = isBanned;
    }

    public string Id { get; set; }
    public string Username { get; set; }
    public string Email { get; set; }
    public bool IsBanned { get; set; }
}