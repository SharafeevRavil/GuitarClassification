using GuitarCogData.Models;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;
using File = GuitarCogData.Models.File;

namespace GuitarCogData;

public class ApplicationDbContext : IdentityDbContext<User>
{
    public ApplicationDbContext(DbContextOptions options) : base(options)
    {
    }

    public DbSet<File> Files { get; set; }
    public DbSet<Tab> Tabs { get; set; }
}