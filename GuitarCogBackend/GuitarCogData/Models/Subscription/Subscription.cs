namespace GuitarCogData.Models.Subscription;

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

    public long Id { get; set; }
    public User User { get; set; }
    public DateTimeOffset Start { get; set; }
    public DateTimeOffset End { get; set; }
    public Payment Payment { get; set; }
}