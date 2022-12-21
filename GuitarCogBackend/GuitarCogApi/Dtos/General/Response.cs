namespace GuitarCogApi.Dtos.General;

/// <summary>
/// Базовый ответ
/// </summary>
public class Response
{
    public Response(string status, string message)
    {
        Status = status;
        Message = message;
    }

    /// <summary>
    /// Статус ответа
    /// </summary>
    public string Status { get; set; }
    /// <summary>
    /// Сообщение ответа
    /// </summary>
    public string Message { get; set; }
}