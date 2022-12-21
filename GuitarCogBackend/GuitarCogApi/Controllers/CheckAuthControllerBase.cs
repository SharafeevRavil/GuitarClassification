using GuitarCogApi.Dtos.General;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;

namespace GuitarCogApi.Controllers;

/// <summary>
/// Базовый класс контроллера, имплементирующий базовую логику получения текущего пользователя
/// </summary>
public abstract class CheckAuthControllerBase : ControllerBase
{
    protected readonly UserManager<User> UserManager;

    protected CheckAuthControllerBase(UserManager<User> userManager)
    {
        UserManager = userManager;
    }

    /// <summary>
    /// Метод проверки аутентификации пользователя
    /// </summary>
    /// <returns>Информация о текущем пользователе</returns>
    [ApiExplorerSettings(IgnoreApi = true)]
    public async Task<(User?, Response?)> CheckAuth()
    {
        var username = User.Identity?.Name;
        if (username == null)
            return (null, new Response("Error", "User not found"));

        var user = await UserManager.FindByNameAsync(username);
        if (user == null)
            return (null, new Response("Error", "User not found"));
        if (user.IsBanned)
            return (null, new Response("Error", "Your account is banned"));

        return (user, null);
    }
}