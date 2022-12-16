using GuitarCogApi.Dtos.Ad;
using GuitarCogApi.Helpers;
using GuitarCogData.Models;

namespace GuitarCogApi.Services;

public class AdService
{
    private readonly SubscriptionService _subscriptionService;

    public AdService(SubscriptionService subscriptionService)
    {
        _subscriptionService = subscriptionService;
    }

    public List<AdListDto> GetAvailableAds(HttpRequest httpRequest, int count = 10)
    {
        var adsPath = Path.Combine(Directory.GetCurrentDirectory(), "StaticFiles", "Ads");
        var adsFiles = new DirectoryInfo(adsPath).GetFiles("index.html", SearchOption.AllDirectories);
        return adsFiles
            .OrderBy(x => Guid.NewGuid())
            .Take(count)
            .Select(x => x.FullName[x.FullName.IndexOf("StaticFiles", StringComparison.Ordinal)..])
            .Select(x => new AdListDto(httpRequest.UriWithBase(x), 300, 250))
            .ToList();
    }

    public bool CheckNeedToShowAds(User user)
    {
        var now = DateTimeOffset.UtcNow;
        return !_subscriptionService.CheckSubscribed(user, now, now).IsSubscribed;
    }
}