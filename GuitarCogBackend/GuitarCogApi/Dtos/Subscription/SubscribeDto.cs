using GuitarCogData.Models.Subscription;

namespace GuitarCogApi.Dtos.Subscription;

/// <summary>
/// Дто подписки
/// </summary>
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

    /// <summary>
    /// Валюта
    /// </summary>
    public Currency Currency { get; set; }
    /// <summary>
    /// Период
    /// </summary>
    public SubscriptionPeriod Period { get; set; }
    /// <summary>
    /// Дата подписки
    /// </summary>
    public DateTimeOffset? StartDate { get; set; }
}