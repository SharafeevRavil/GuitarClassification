using GuitarCogApi.Dtos.General;
using Microsoft.EntityFrameworkCore;

namespace GuitarCogApi.Helpers;

public static class PageHelper
{
    public static async Task<PagedResponse<T>> PagedResponse<T>(this IQueryable<T> data, int page, int pageSize)
    {
        var respData = await data.Skip((page - 1) * pageSize).Take(pageSize).ToListAsync();
        var count = await data.CountAsync();
        
        var pageCount = (int)Math.Ceiling((double)count / pageSize);
        return new PagedResponse<T>(respData, page, pageCount, count);
    }
}