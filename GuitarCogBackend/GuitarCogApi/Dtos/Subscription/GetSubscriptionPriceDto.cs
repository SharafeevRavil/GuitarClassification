using GuitarCogData.Models.Subscription;

namespace GuitarCogApi.Dtos.Subscription;

/// <summary>
/// Дто запроса цены подписки
/// </summary>
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

    /// <summary>
    /// Валюты
    /// </summary>
    public List<Currency> Currencies { get; set; } = null!;
    /// <summary>
    /// Периоды подписки
    /// </summary>
    public List<SubscriptionPeriod> Periods { get; set; } = null!;
    /// <summary>
    /// Дата начала подписки
    /// </summary>
    public DateTimeOffset? StartDate { get; set; }
}