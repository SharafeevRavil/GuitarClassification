using System.Text.Json.Serialization;

namespace GuitarCogData.Models.Subscription;

public struct Money
{
    [JsonConstructor]
    public Money(decimal amount, Currency currency)
    {
        Amount = amount;
        Currency = currency;
    }

    public decimal Amount { get; set; }
    public Currency Currency { get; set; }
}