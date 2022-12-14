using GuitarCogApi.Dtos.General;

namespace GuitarCogApi.Helpers;

public static class PageHelper
{
    public static PagedResponse<T> PagedResponse<T>(this IQueryable<T> data, int page, int pageSize)
    {
        var respData = data.Skip((page - 1) * pageSize).Take(pageSize).ToList();
        var count = data.Count();
        var pageCount = (int)Math.Ceiling((double)count / pageSize);
        return new PagedResponse<T>(respData, page, pageCount, count);
    }
}