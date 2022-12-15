using GuitarCogData.Models.Subscription;

namespace GuitarCogApi.Dtos.Subscription;

public class SubscribeDto
{
    public SubscribeDto(Currency currency, SubscriptionPeriod period)
    {
        Currency = currency;
        Period = period;
    }

    public SubscribeDto()
    {
        
    }

    public Currency Currency { get; set; }
    public SubscriptionPeriod Period { get; set; }
    public DateTimeOffset? StartDate { get; set; }
}