using System.ComponentModel.DataAnnotations.Schema;

namespace GuitarCogData.Models.Subscription;

public class Payment
{
    public Payment(DateTimeOffset createDate, Money money)
    {
        CreateDate = createDate;
        
        MoneyAmount = money.Amount;
        MoneyCurrency = money.Currency;
    }

    public Payment()
    {
        
    }

    public long Id { get; set; }
    public DateTimeOffset CreateDate { get; set; }
    public DateTimeOffset? PayDate { get; set; }
    
    public decimal MoneyAmount { get; set; }
    public Currency MoneyCurrency { get; set; }
}