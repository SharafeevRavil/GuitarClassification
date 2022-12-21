namespace GuitarCogApi.Dtos.Subscription;

/// <summary>
/// Дто результата подписки
/// </summary>
public class SubscribeResultDto
{
    public SubscribeResultDto(DateTimeOffset subscriptionStart, DateTimeOffset subscriptionEnd)
    {
        SubscriptionStart = subscriptionStart;
        SubscriptionEnd = subscriptionEnd;
    }

    /// <summary>
    /// Дата начала
    /// </summary>
    public DateTimeOffset SubscriptionStart { get; set; }
    /// <summary>
    /// Дата окончания
    /// </summary>
    public DateTimeOffset SubscriptionEnd { get; set; }
}