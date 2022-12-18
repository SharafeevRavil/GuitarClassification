using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Moder.ModerUser;
using GuitarCogApi.Helpers;
using GuitarCogData;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Identity;

namespace GuitarCogApi.Services.Moder;

public class ModerUserService
{
    private readonly ApplicationDbContext _dbContext;
    private readonly UserService _userService;
    private readonly UserManager<User> _userManager;

    public ModerUserService(ApplicationDbContext dbContext, UserService userService, UserManager<User> userManager)
    {
        _dbContext = dbContext;
        _userService = userService;
        _userManager = userManager;
    }

    public async Task<PagedResponse<ModerUserListDto>> GetUsers(PagedFilter pagedFilter) =>
        await _dbContext.Users
            .Select(x => new ModerUserListDto(x.Id, x.UserName!, x.Email!))
            .PagedResponse(pagedFilter.Page ?? 1, pagedFilter.PageSize ?? 10);

    public async Task<(User?, Response?)> CreateModer(CreateModerDto dto)
    {
        var (user, response) = await _userService.CreateUser(dto.Username, dto.Email, dto.Password);
        if (response != null || user == null)
            return (null, response ?? new Response("Error", "Cannot create moder. Try later."));

        await _userManager.AddToRoleAsync(user, $"{Role.Moderator}");
        return (user, null);
    }
}