using System.ComponentModel.DataAnnotations.Schema;

namespace GuitarCogData.Models.Subscription;

/// <summary>
/// Цена подписки
/// </summary>
public class SubscriptionPrice
{
    public SubscriptionPrice(Money money, SubscriptionPeriod subscriptionPeriod,
        DateTimeOffset createDate, DateTimeOffset start, DateTimeOffset end)
    {
        MoneyAmount = money.Amount;
        MoneyCurrency = money.Currency;
        CreateDate = createDate;
        Start = start;
        End = end;
        SubscriptionPeriod = subscriptionPeriod;
    }

    public SubscriptionPrice()
    {
        
    }

    /// <summary>
    /// Id
    /// </summary>
    public long Id { get; set; }
    /// <summary>
    /// Сумма денег
    /// </summary>
    public decimal MoneyAmount { get; set; }
    /// <summary>
    /// Валюта оплаты
    /// </summary>
    public Currency MoneyCurrency { get; set; }
    /// <summary>
    /// Период подписки
    /// </summary>
    public SubscriptionPeriod SubscriptionPeriod { get; set; }
    /// <summary>
    /// Создание цены
    /// </summary>
    public DateTimeOffset CreateDate { get; set; }
    /// <summary>
    /// Начало действия цены
    /// </summary>
    public DateTimeOffset Start { get; set; }
    /// <summary>
    /// Конец действия цены
    /// </summary>
    public DateTimeOffset End { get; set; }
}