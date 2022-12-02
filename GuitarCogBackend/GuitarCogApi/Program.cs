using GuitarCogApi.Initializers;using GuitarCogData;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);
if(!builder.Environment.IsDevelopment())
    builder.WebHost.UseUrls($"http://*:{builder.Configuration.GetValue<int>("PORT")}");

Console.WriteLine($"PORT IS {builder.Configuration.GetValue<int>("PORT")} WTFFFF");

// Add services to the container.

builder.Services.AddDbContext<ApplicationDbContext>(options =>
{
    options.UseNpgsql(
        builder.Environment.IsDevelopment()
    ? builder.Configuration.GetConnectionString("DefaultConnection")
    : $"Host={builder.Configuration["PGHOST"]};Port={builder.Configuration["PGPORT"]};" +
      $"Username={builder.Configuration["PGUSER"]};Password={builder.Configuration["PGPASSWORD"]};" +
      $"Database={builder.Configuration["PGDATABASE"]}");
});

builder.Services.AddAuthentication();
builder.Services.AddIdentity<User, IdentityRole>(o =>
    {
        o.Password.RequireDigit = false;
        o.Password.RequireLowercase = false;
        o.Password.RequireUppercase = false;
        o.Password.RequireNonAlphanumeric = false;
        o.User.RequireUniqueEmail = true;
    })
    .AddEntityFrameworkStores<ApplicationDbContext>()
    .AddDefaultTokenProviders();


builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

if (app.Configuration.GetValue<bool>("NEED_MIGRATIONS"))
{
    DatabaseInitializer.UpdateDatabase(app);
}

app.UseAuthentication();
app.UseAuthorization();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

/*if(builder.Environment.IsDevelopment())
    app.Run();
else
    app.Run($"http://0.0.0.0:{builder.Configuration.GetValue<int>("PORT")}");*/

app.Run();

await DatabaseInitializer.EnsureDatabaseValid(app);