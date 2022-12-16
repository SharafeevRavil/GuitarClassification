namespace GuitarCogApi.Helpers;

public static class UriHelper
{
    public static Uri BaseUri(this HttpRequest httpRequest) => 
        new Uri($"{httpRequest.Scheme}://{httpRequest.Host}");
    
    public static string UriWithBase(this HttpRequest httpRequest, string relativeUri) => 
        new Uri(new Uri($"{httpRequest.Scheme}://{httpRequest.Host}"), relativeUri).ToString();
}