namespace GuitarCogApi.Dtos.Ad;

/// <summary>
/// Дто рекламы
/// </summary>
public class AdDto
{
    public AdDto(bool needToShowAds, List<AdListDto>? ads)
    {
        NeedToShowAds = needToShowAds;
        Ads = ads;
    }

    /// <summary>
    /// Нужно ли показывать релкаму пользователю
    /// </summary>
    public bool NeedToShowAds { get; set; }
    /// <summary>
    /// Список баннеров
    /// </summary>
    public List<AdListDto>? Ads { get; set; }
}