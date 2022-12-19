namespace GuitarCogApi.Dtos.Tab;

public class TabLimitDto
{
    public TabLimitDto(int tabCount, int tabLimit)
    {
        TabCount = tabCount;
        TabLimit = tabLimit;
    }

    /// <summary> Текущее количество табов </summary>
    public int TabCount { get; set; }
    /// <summary> Лимит табов </summary>
    public int TabLimit { get; set; }
}