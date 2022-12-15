using System.ComponentModel.DataAnnotations.Schema;

namespace GuitarCogData.Models.Subscription;

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

    public long Id { get; set; }
    
    
    public decimal MoneyAmount { get; set; }
    public Currency MoneyCurrency { get; set; }
    
    public SubscriptionPeriod SubscriptionPeriod { get; set; }
    public DateTimeOffset CreateDate { get; set; }
    public DateTimeOffset Start { get; set; }
    public DateTimeOffset End { get; set; }
}