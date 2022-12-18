using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Moder.ModerUser;
using GuitarCogApi.Dtos.Subscription;
using GuitarCogApi.Helpers;
using GuitarCogData;
using GuitarCogData.Models;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;

namespace GuitarCogApi.Services.Moder;

public class ModerUserService
{
    private readonly ApplicationDbContext _dbContext;
    private readonly UserService _userService;
    private readonly UserManager<User> _userManager;
    private readonly FileService _fileService;
    private SubscriptionService _subscriptionService;

    public ModerUserService(ApplicationDbContext dbContext, UserService userService, UserManager<User> userManager,
        FileService fileService, SubscriptionService subscriptionService)
    {
        _dbContext = dbContext;
        _userService = userService;
        _userManager = userManager;
        _fileService = fileService;
        _subscriptionService = subscriptionService;
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

    public async Task<(ModerUserDto?, Response?)> GetUser(HttpRequest request, string userId)
    {
        var user = await _dbContext.Users
            .Include(x => x.AvatarImage)
            .FirstOrDefaultAsync(x => x.Id == userId);

        if (user == null)
            return (null, new Response("Error", $"Can't find user with id {userId}"));

        var avatarUrl = user.AvatarImage != null
            ? _fileService.GetUrlByFileId(request, user.AvatarImage!.Id)
            : "";

        var subscription = await _subscriptionService.CheckSubscribed(user);
        var roles = await _userManager.GetRolesAsync(user);
        
        var dto = new ModerUserDto(user.Id, user.UserName!, user.Email!, avatarUrl, subscription, roles);
        return (dto, null);
    }
}