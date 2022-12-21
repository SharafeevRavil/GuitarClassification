using System.Text.Json.Serialization;

namespace GuitarCogData.Models.Subscription;

/// <summary>
/// Деньги за подписку
/// </summary>
public struct Money
{
    [JsonConstructor]
    public Money(decimal amount, Currency currency)
    {
        Amount = amount;
        Currency = currency;
    }
    /// <summary>
    /// Сумма, внесённая за подписку
    /// </summary>
    public decimal Amount { get; set; }
    /// <summary>
    /// Валюта оплаты
    /// </summary>
    public Currency Currency { get; set; }
}