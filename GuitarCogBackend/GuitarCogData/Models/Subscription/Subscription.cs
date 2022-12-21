namespace GuitarCogData.Models.Subscription;

/// <summary>
/// Подписка
/// </summary>
public class Subscription
{
    public Subscription(User user, DateTimeOffset start, DateTimeOffset end, Payment payment)
    {
        User = user;
        Start = start;
        End = end;
        Payment = payment;
    }

    public Subscription()
    {
        
    }

    /// <summary>
    /// Id
    /// </summary>
    public long Id { get; set; }
    /// <summary>
    /// Пользователь
    /// </summary>
    public User User { get; set; }
    /// <summary>
    /// Начало подписки
    /// </summary>
    public DateTimeOffset Start { get; set; }
    /// <summary>
    /// Конец подписки
    /// </summary>
    public DateTimeOffset End { get; set; }
    /// <summary>
    /// Оплата подписки
    /// </summary>
    public Payment Payment { get; set; }
}