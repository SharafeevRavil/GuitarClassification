namespace GuitarCogApi.Dtos.Ad;

public class AdDto
{
    public AdDto(bool needToShowAds, List<AdListDto>? ads)
    {
        NeedToShowAds = needToShowAds;
        Ads = ads;
    }

    public bool NeedToShowAds { get; set; }
    public List<AdListDto>? Ads { get; set; }
}