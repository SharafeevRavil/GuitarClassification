using GuitarCogData;
using GuitarCogData.Models;
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

        var userManager = serviceProvider.GetRequiredService<UserManager<User>>();
        var roleManager = serviceProvider.GetRequiredService<RoleManager<IdentityRole>>();

        string[] roleNames = {"SuperAdmin", "Moderator"};
        foreach (var roleName in roleNames)
        {
            if (!await roleManager.RoleExistsAsync(roleName))
            {
                await roleManager.CreateAsync(new IdentityRole(roleName));
            }
        }

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
}