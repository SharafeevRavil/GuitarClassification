namespace GuitarCogApi.Dtos.Profile;

public class ProfileDto
{
    public ProfileDto(string id, string username, string email, string imageUrl)
    {
        Id = id;
        Username = username;
        Email = email;
        ImageUrl = imageUrl;
    }

    public string Id { get; set; }
    public string Username { get; set; }
    public string Email { get; set; }
    public string ImageUrl { get; set; }
}