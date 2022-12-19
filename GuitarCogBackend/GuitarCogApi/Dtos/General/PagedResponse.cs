namespace GuitarCogApi.Dtos.General;

public class PagedResponse<T>
{
    public PagedResponse(List<T> data, int page, int pageCount, int elementsCount)
    {
        Data = data;
        Page = page;
        PageCount = pageCount;
        ElementsCount = elementsCount;
    }

    public int Page { get; set; }
    public int PageCount { get; set; }
    public int ElementsCount { get; set; }
    
    public List<T> Data { get; set; }
}