using System.Text.Json;
using GuitarCogData.Models;
using GuitarCogData.Models.Subscription;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;
using File = GuitarCogData.Models.File;

namespace GuitarCogData;

public class ApplicationDbContext : IdentityDbContext<User>
{
    public ApplicationDbContext(DbContextOptions options) : base(options)
    {
    }

    protected override void OnModelCreating(ModelBuilder builder)
    {
        base.OnModelCreating(builder);
    }

    public DbSet<File> Files { get; set; }
    public DbSet<Tab> Tabs { get; set; }
    public DbSet<Report> Report { get; set; }
    
    //Subscription
    public DbSet<SubscriptionPrice> SubscriptionPrices { get; set; }
    public DbSet<Payment> Payments { get; set; }
    public DbSet<Subscription> Subscriptions { get; set; }
}