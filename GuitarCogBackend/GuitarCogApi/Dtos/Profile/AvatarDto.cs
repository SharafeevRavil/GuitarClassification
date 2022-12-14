namespace GuitarCogApi.Dtos.Profile;

public class AvatarDto
{
    public AvatarDto(string avatarUrl)
    {
        AvatarUrl = avatarUrl;
    }

    public string AvatarUrl { get; set; }
}