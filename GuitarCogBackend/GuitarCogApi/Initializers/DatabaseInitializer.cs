using GuitarCogData;
using GuitarCogData.Models;
using GuitarCogData.Models.Subscription;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;

namespace GuitarCogApi.Initializers;

public static class DatabaseInitializer
{
    public static void UpdateDatabase(IApplicationBuilder app)
    {
        using var serviceScope = app.ApplicationServices
            .GetRequiredService<IServiceScopeFactory>()
            .CreateScope();
        using var context = serviceScope.ServiceProvider.GetService<ApplicationDbContext>();

        if (context == null)
            throw new Exception("context is null");

        context.Database.Migrate();
    }
    
    public static async Task EnsureDatabaseValid(IApplicationBuilder app)
    {
        var serviceProvider = app.ApplicationServices
            .CreateScope().ServiceProvider.GetService<IServiceProvider>();

        if (serviceProvider == null)
            throw new Exception("serviceProvider is null");

        await EnsureRolesExist(serviceProvider);
        await EnsureSuperAdminCreated(serviceProvider);
        await EnsureSubscriptionPricesCreated(serviceProvider);
    }

    private static async Task EnsureSuperAdminCreated(IServiceProvider serviceProvider)
    {
        var userManager = serviceProvider.GetRequiredService<UserManager<User>>();
        var admin = await userManager.FindByEmailAsync("admin@mail.ru");
        if (admin == null)
        {
            admin = new User
            {
                UserName = "Admin",
                Email = "admin@mail.ru",
                Id = Guid.NewGuid().ToString(),
            };
            var createPowerUser = await userManager.CreateAsync(admin, "Admin123!");
            if (createPowerUser.Succeeded)
            {
                await userManager.AddToRoleAsync(admin, "SuperAdmin");
                var token = await userManager.GenerateEmailConfirmationTokenAsync(admin);
                await userManager.ConfirmEmailAsync(admin, token);
            }
        }
    }

    private static async Task EnsureRolesExist(IServiceProvider serviceProvider)
    {
        var roleManager = serviceProvider.GetRequiredService<RoleManager<IdentityRole>>();

        string[] roleNames = { "SuperAdmin", "Moderator" };
        foreach (var roleName in roleNames)
        {
            if (!await roleManager.RoleExistsAsync(roleName))
            {
                await roleManager.CreateAsync(new IdentityRole(roleName));
            }
        }
    }

    private static async Task EnsureSubscriptionPricesCreated(IServiceProvider serviceProvider)
    {
        var dbContext = serviceProvider.GetRequiredService<ApplicationDbContext>();
        
        const decimal eurM = 1.5m;
        const decimal rubM = 100;
        const decimal usdM = 2;

        var today = new DateTimeOffset(DateTimeOffset.UtcNow.Date, TimeSpan.Zero).ToUniversalTime();
        var afterYear = today.AddYears(1);

        var subscriptionPrices = new []
        {
            new SubscriptionPrice(new Money(rubM, Currency.Rub), SubscriptionPeriod.Month,today, today, afterYear),
            new SubscriptionPrice(new Money(eurM, Currency.Eur), SubscriptionPeriod.Month, today, today, afterYear),
            new SubscriptionPrice(new Money(usdM, Currency.Usd), SubscriptionPeriod.Month, today, today, afterYear),
            
            new SubscriptionPrice(new Money(rubM*5.5m, Currency.Rub), SubscriptionPeriod.HalfOfYear,today, today, afterYear),
            new SubscriptionPrice(new Money(eurM*5.5m, Currency.Eur), SubscriptionPeriod.HalfOfYear, today, today, afterYear),
            new SubscriptionPrice(new Money(usdM*5.5m, Currency.Usd), SubscriptionPeriod.HalfOfYear, today, today, afterYear),
            
            new SubscriptionPrice(new Money(rubM*10, Currency.Rub), SubscriptionPeriod.Year,today, today, afterYear),
            new SubscriptionPrice(new Money(eurM*10, Currency.Eur), SubscriptionPeriod.Year, today, today, afterYear),
            new SubscriptionPrice(new Money(usdM*10, Currency.Usd), SubscriptionPeriod.Year, today, today, afterYear),
        };

        var toAdd = new List<SubscriptionPrice>();
        
        foreach (var c in (Currency[]) Enum.GetValues(typeof(Currency)))
        {
            foreach (var sp in (SubscriptionPeriod[]) Enum.GetValues(typeof(SubscriptionPeriod)))
            {
                if (!dbContext.SubscriptionPrices.Any(x => x.Start <= today && today <= x.End && 
                                                           x.SubscriptionPeriod == sp && x.MoneyCurrency == c))
                {
                    dbContext.SubscriptionPrices.Add(subscriptionPrices
                        .First(x => x.SubscriptionPeriod == sp && x.MoneyCurrency == c));
                }
            }
        }
        
        await dbContext.SaveChangesAsync();
    }
}