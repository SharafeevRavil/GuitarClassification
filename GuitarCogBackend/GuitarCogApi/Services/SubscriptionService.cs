using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Subscription;
using GuitarCogData;
using GuitarCogData.Models;
using GuitarCogData.Models.Subscription;
using Microsoft.EntityFrameworkCore;

namespace GuitarCogApi.Services;

public class SubscriptionService
{
    private ApplicationDbContext _dbContext;

    public SubscriptionService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    /// <summary>
    /// Получение цены за подписку
    /// </summary>
    /// <param name="getSubscriptionPriceDto"></param>
    /// <returns></returns>
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

    /// <summary>
    /// Получение и сортировка цен для даты
    /// </summary>
    /// <param name="startDate"></param>
    /// <returns></returns>
    //берем последнюю актуальную (*.Start < startDate < *.End) или просроченную (*.Start < startDate)
    //UPD: не, это хуйня, лучше не выдавать просроченные
    private IOrderedQueryable<SubscriptionPrice> PricesByDate(DateTimeOffset startDate) =>
        _dbContext.SubscriptionPrices
            .Where(x => x.Start <= startDate && startDate <= x.End)
            .OrderByDescending(x => x.Start);

    /// <summary>
    /// Подписка пользователя на сервис
    /// </summary>
    /// <param name="user"></param>
    /// <param name="subscribeDto"></param>
    /// <returns></returns>
    /// <exception cref="ArgumentOutOfRangeException"></exception>
    public async Task<(SubscribeResultDto?, Response?)> Subscribe(User user, SubscribeDto subscribeDto)
    {
        var inputStartDate = subscribeDto.StartDate!.Value.ToUniversalTime();
        var period = subscribeDto.Period;
        var currency = subscribeDto.Currency;

        
        var start = new DateTimeOffset(inputStartDate.Date, TimeSpan.Zero).ToUniversalTime();
        var end = period switch
        {
            SubscriptionPeriod.Month => start.AddMonths(1).AddSeconds(-1),
            SubscriptionPeriod.HalfOfYear => start.AddMonths(6).AddSeconds(-1),
            SubscriptionPeriod.Year => start.AddMonths(12).AddSeconds(-1),
            _ => throw new ArgumentOutOfRangeException(nameof(period), period, null)
        };

        var isSubscribedForPeriod = await CheckSubscribed(user, start, end);
        if (isSubscribedForPeriod.IsSubscribed)
            return (null, new Response("Error", "multiple subscription for a period is not allowed"));
        
        var ordered = PricesByDate(start);
        var sp = ordered
            .FirstOrDefault(sp => sp.MoneyCurrency == currency && sp.SubscriptionPeriod == period);
        if (sp == null)
            return (null,
                new Response("Error", "subscription price was not found for specified currency, period and date"));

        var payment = new Payment(DateTimeOffset.UtcNow, new Money(sp.MoneyAmount, sp.MoneyCurrency));
        var subscriptionEntry = _dbContext.Subscriptions.Add(new Subscription(user, start, end, payment));
        //автооплата
        payment.PayDate = DateTimeOffset.UtcNow;
        await _dbContext.SaveChangesAsync();

        return (new SubscribeResultDto(subscriptionEntry.Entity.Start, subscriptionEntry.Entity.End), null);
    }

    /// <summary>
    /// Проверка статуса подписки
    /// </summary>
    /// <param name="user"></param>
    /// <param name="start"></param>
    /// <param name="end"></param>
    /// <returns></returns>
    public async Task<SubscriptionInfoDto> CheckSubscribed(User user, DateTimeOffset start, DateTimeOffset end)
    {
        start = start.ToUniversalTime();
        end = end.ToUniversalTime();
        var subscription = await _dbContext.Subscriptions
            .Include(x => x.Payment)
            .Include(x => x.User)
            .OrderByDescending(x => x.End)
            .FirstOrDefaultAsync(x => x.User.Id == user.Id && x.Payment.PayDate != null &&
                                 //чек на пересечение отрезка
                                 (x.Start <= start && start <= x.End || //наш старт в промежутке
                                  x.Start <= end && end <= x.End || //наш конец в промежутке
                                  start <= x.Start && x.End <= end) //промежуток между стартом и концом
            );
        return subscription != null
            ? new SubscriptionInfoDto(true, subscription.Start, subscription.End)
            : new SubscriptionInfoDto(false);
    }

    /// <summary>
    /// Проверка статуса подписки в определённный момент
    /// </summary>
    /// <param name="user"></param>
    /// <param name="startAndEnd"></param>
    /// <returns></returns>
    public async Task<SubscriptionInfoDto> CheckSubscribed(User user, DateTimeOffset startAndEnd) => await CheckSubscribed(user, startAndEnd, startAndEnd);

    /// <summary>
    /// Проверка статуса подписки в данный момент
    /// </summary>
    /// <param name="user"></param>
    /// <returns></returns>
    public async Task<SubscriptionInfoDto> CheckSubscribed(User user) => await CheckSubscribed(user, DateTimeOffset.UtcNow);
}