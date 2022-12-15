using GuitarCogData.Models.Subscription;

namespace GuitarCogApi.Dtos.Subscription;

public class GetSubscriptionPriceDto
{
    public GetSubscriptionPriceDto(List<Currency> currencies, List<SubscriptionPeriod> periods, DateTimeOffset startDate)
    {
        Currencies = currencies;
        Periods = periods;
        StartDate = startDate;
    }

    public GetSubscriptionPriceDto()
    {
        
    }

    public List<Currency> Currencies { get; set; }
    public List<SubscriptionPeriod> Periods { get; set; }
    public DateTimeOffset? StartDate { get; set; }
}