using GuitarCogData.Models.Subscription;

namespace GuitarCogApi.Dtos.Subscription;

/// <summary>
/// Дто возвращённой цены подписки
/// </summary>
public class SubscriptionPriceDto
{
    public SubscriptionPriceDto(Money money, SubscriptionPeriod subscriptionPeriod)
    {
        Money = money;
        SubscriptionPeriod = subscriptionPeriod;
    }

    /// <summary>
    /// Цена подписки
    /// </summary>
    public Money Money { get; set; }
    /// <summary>
    /// Период подписки
    /// </summary>
    public SubscriptionPeriod SubscriptionPeriod { get; set; }
}