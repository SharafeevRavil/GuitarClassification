namespace GuitarCogApi.Dtos.Subscription;

public class SubscriptionInfoDto
{
    public SubscriptionInfoDto(bool isSubscribed, DateTimeOffset? start = null, DateTimeOffset? end = null)
    {
        IsSubscribed = isSubscribed;
        Start = start;
        End = end;
    }

    public bool IsSubscribed { get; set; }
    public DateTimeOffset? Start { get; set; }
    public DateTimeOffset? End { get; set; }
}