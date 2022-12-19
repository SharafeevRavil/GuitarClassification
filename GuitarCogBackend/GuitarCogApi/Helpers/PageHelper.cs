using GuitarCogApi.Dtos.General;
using Microsoft.EntityFrameworkCore;

namespace GuitarCogApi.Helpers;

public static class PageHelper
{
    public static async Task<PagedResponse<T>> PagedResponse<T>(this IQueryable<T> data, int page, int pageSize)
    {
        if (page <= 0) page = 1;
        if (pageSize == 0)
            throw new ArgumentException(nameof(pageSize));

        var count = await data.CountAsync();
        if (count == 0)
            return new PagedResponse<T>(new List<T>(), 1, 1, 0);

        var minElementsCountToCurPage = (page - 1) * pageSize + 1;
        if (count < minElementsCountToCurPage)
            //не хватает элементов - возвращаю последнюю страницу
            page = (count - 1) / pageSize + 1;

        var respData = await data.Skip((page - 1) * pageSize).Take(pageSize).ToListAsync();
        
        var pageCount = (int)Math.Ceiling((double)count / pageSize);
        return new PagedResponse<T>(respData, page, pageCount, count);
    }
}