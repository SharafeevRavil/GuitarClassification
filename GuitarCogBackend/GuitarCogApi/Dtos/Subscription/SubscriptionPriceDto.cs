using GuitarCogData.Models.Subscription;

namespace GuitarCogApi.Dtos.Subscription;

public class SubscriptionPriceDto
{
    public SubscriptionPriceDto(Money money, SubscriptionPeriod subscriptionPeriod)
    {
        Money = money;
        SubscriptionPeriod = subscriptionPeriod;
    }

    public Money Money { get; set; }
    public SubscriptionPeriod SubscriptionPeriod { get; set; }
}