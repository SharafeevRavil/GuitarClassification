namespace GuitarCogApi.Dtos.Moder.ModerUser;

public class ModerUserListDto
{
    public ModerUserListDto(string id, string username, string email)
    {
        Id = id;
        Username = username;
        Email = email;
    }

    public string Id { get; set; }
    public string Username { get; set; }
    public string Email { get; set; }
}