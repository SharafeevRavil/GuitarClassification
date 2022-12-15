namespace GuitarCogApi.Dtos.Subscription;

public class SubscribeResultDto
{
    public SubscribeResultDto(DateTimeOffset subscriptionStart, DateTimeOffset subscriptionEnd)
    {
        SubscriptionStart = subscriptionStart;
        SubscriptionEnd = subscriptionEnd;
    }

    public DateTimeOffset SubscriptionStart { get; set; }
    public DateTimeOffset SubscriptionEnd { get; set; }
}