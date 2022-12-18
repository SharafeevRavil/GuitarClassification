using GuitarCogApi.Dtos.General;
using GuitarCogApi.Dtos.Moder.ModerUser;
using GuitarCogApi.Helpers;
using GuitarCogData;

namespace GuitarCogApi.Services.Moder;

public class ModerUserService
{
    private readonly ApplicationDbContext _dbContext;

    public ModerUserService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    public async Task<PagedResponse<ModerUserListDto>> GetUsers(PagedFilter pagedFilter) =>
        await _dbContext.Users
            .Select(x => new ModerUserListDto(x.Id, x.UserName!, x.Email!))
            .PagedResponse(pagedFilter.Page ?? 1, pagedFilter.PageSize ?? 10);
}