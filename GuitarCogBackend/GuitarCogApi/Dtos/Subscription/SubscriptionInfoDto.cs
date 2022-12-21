namespace GuitarCogApi.Dtos.Subscription;

/// <summary>
/// Дто статуса подписки
/// </summary>
public class SubscriptionInfoDto
{
    public SubscriptionInfoDto(bool isSubscribed, DateTimeOffset? start = null, DateTimeOffset? end = null)
    {
        IsSubscribed = isSubscribed;
        Start = start;
        End = end;
    }

    /// <summary>
    /// Статус подписки
    /// </summary>
    public bool IsSubscribed { get; set; }
    /// <summary>
    /// Дата начала подписки
    /// </summary>
    public DateTimeOffset? Start { get; set; }
    /// <summary>
    /// Дата окончания подписки
    /// </summary>
    public DateTimeOffset? End { get; set; }
}