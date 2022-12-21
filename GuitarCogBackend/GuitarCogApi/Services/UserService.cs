using GuitarCogApi.Dtos.General;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Identity;

namespace GuitarCogApi.Services;

public class UserService
{
    private readonly UserManager<User> _userManager;

    public UserService(UserManager<User> userManager)
    {
        _userManager = userManager;
    }

    /// <summary>
    /// Создание пользователя
    /// </summary>
    /// <param name="username"></param>
    /// <param name="email"></param>
    /// <param name="password"></param>
    /// <returns></returns>
    public async Task<(User?, Response?)> CreateUser(string username, string email, string password)
    {
        var userExists = await _userManager.FindByNameAsync(username);
        if (userExists != null)
            return (null, new Response("Error", "User already exists!"));

        User user = new()
        {
            Email = email,
            SecurityStamp = Guid.NewGuid().ToString(),
            UserName = username
        };
        var result = await _userManager.CreateAsync(user, password);
        if (!result.Succeeded)
        {
            var errors = result.Errors
                .Select(x => $"[{x.Code}] {x.Description}")
                .Aggregate((a, b) => $"{a}\n{b}");
            return (null, new Response(nameof(StatusCodes.Status500InternalServerError), $"User creation failed! Errors:\n{errors}"));
        }

        return (user, null);
    }
}