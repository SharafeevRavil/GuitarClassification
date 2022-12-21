using System.ComponentModel.DataAnnotations.Schema;

namespace GuitarCogData.Models.Subscription;

/// <summary>
/// Оплата подписки
/// </summary>
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

    /// <summary>
    /// Id
    /// </summary>
    public long Id { get; set; }
    /// <summary>
    /// Дата оформления платежа
    /// </summary>
    public DateTimeOffset CreateDate { get; set; }
    /// <summary>
    /// Дата оплаты
    /// </summary>
    public DateTimeOffset? PayDate { get; set; }
    /// <summary>
    /// Сумма денег
    /// </summary>
    public decimal MoneyAmount { get; set; }
    /// <summary>
    /// Валюта оплаты
    /// </summary>
    public Currency MoneyCurrency { get; set; }
}