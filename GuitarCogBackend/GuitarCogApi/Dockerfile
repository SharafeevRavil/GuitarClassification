FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS base
WORKDIR /app
#EXPOSE 80
#EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build

WORKDIR /src
COPY ["GuitarCogApi/GuitarCogApi.csproj", "GuitarCogApi/", "GuitarCogData/"]
RUN dotnet restore "GuitarCogApi/GuitarCogApi.csproj"
COPY . .
WORKDIR "/src/GuitarCogApi"
RUN dotnet build "GuitarCogApi.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "GuitarCogApi.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
#ENTRYPOINT ["dotnet", "GuitarCogApi.dll"]
# heroku uses the following
CMD ASPNETCORE_URLS=http://*:$PORT dotnet GuitarCogApi.dll
