using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Subscription;
using GuitarCogData;
using GuitarCogData.Models;
using GuitarCogData.Models.Subscription;

namespace GuitarCogApi.Services;

public class SubscriptionService
{
    private ApplicationDbContext _dbContext;

    public SubscriptionService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    public List<SubscriptionPriceDto> GetPriceForPeriod(GetSubscriptionPriceDto getSubscriptionPriceDto)
    {
        var startDate = getSubscriptionPriceDto.StartDate!.Value.ToUniversalTime();
        var ordered = PricesByDate(startDate);
        return getSubscriptionPriceDto.Currencies
            .SelectMany(c => getSubscriptionPriceDto.Periods
                .Select(p =>
                    ordered.FirstOrDefault(sp => sp.MoneyCurrency == c && sp.SubscriptionPeriod == p)))
            .Where(x => x != null)
            .Select(x => new SubscriptionPriceDto(new Money(x!.MoneyAmount, x.MoneyCurrency), x.SubscriptionPeriod))
            .ToList();
    }

    //берем последнюю актуальную (*.Start < startDate < *.End) или просроченную (*.Start < startDate)
    //UPD: не, это хуйня, лучше не выдавать просроченные
    private IOrderedQueryable<SubscriptionPrice> PricesByDate(DateTimeOffset startDate) =>
        _dbContext.SubscriptionPrices
            .Where(x => x.Start <= startDate && startDate <= x.End)
            .OrderByDescending(x => x.Start);

    public async Task<(SubscribeResultDto?, Response?)> Subscribe(User user, SubscribeDto subscribeDto)
    {
        var startDate = subscribeDto.StartDate!.Value.ToUniversalTime();
        var period = subscribeDto.Period;
        var currency = subscribeDto.Currency;

        var ordered = PricesByDate(startDate);
        var sp = ordered
            .FirstOrDefault(sp => sp.MoneyCurrency == currency && sp.SubscriptionPeriod == period);
        if (sp == null)
            return (null,
                new Response("Error", "subscription price was not found for specified currency, period and date"));

        var start = new DateTimeOffset(startDate.Date, TimeSpan.Zero).ToUniversalTime();
        var end = period switch
        {
            SubscriptionPeriod.Month => start.AddMonths(1).AddSeconds(-1),
            SubscriptionPeriod.HalfOfYear => start.AddMonths(6).AddSeconds(-1),
            SubscriptionPeriod.Year => start.AddMonths(12).AddSeconds(-1),
            _ => throw new ArgumentOutOfRangeException(nameof(period), period, null)
        };
        var payment = new Payment(DateTimeOffset.UtcNow, new Money(sp.MoneyAmount, sp.MoneyCurrency));
        var subscriptionEntry = _dbContext.Subscriptions.Add(new Subscription(user, start, end, payment));
        //автооплата
        payment.PayDate = DateTimeOffset.UtcNow;
        await _dbContext.SaveChangesAsync();

        return (new SubscribeResultDto(subscriptionEntry.Entity.Start, subscriptionEntry.Entity.End), null);
    }
}