# Backend
Проекты в решении:
* GuitarCogApi - проект с ASP.NET API
* GuitarCogData - проект с ApplicationDbContext и сущностями

## Установка .NET SDK и среды разработки
Для разработки рекомендуется использовать Rider или подходящую IDE, поддерживающую работу с C# и .NET.

Необходимо установить .NET SDK 7.

## Начало работы:
При разработке использовать конфигурацию `GuitarCogApi: https`, настраивать в `appsettings.json` или `appsettings.Development.json`

При деплое:
1) Указать среду `ASPNETCORE_ENVIRONMENT` = `Development`/`Staging`/`Production`
2) Указать connection string для бд - переменные среды `PGDATABASE`, `PGHOST`, `PGPASSWORD`, `PGPORT`, `PGUSER`
3) Указать, нужно ли накатывать миграции при запуске приложения `NEED_MIGRATIONS` = `true`/`false`
4) Запускать / следовать инструкциям из `Dockerfile`

## Миграции
Для миграций с помощью следующих команд будет использоваться конфигурация бд из `Program.cs`

Для создания миграции:
1) перейти в корневую папку решения (папку с файлом GuitarCogBackend.sln)
2) `dotnet ef migrations add "НАЗВАНИЕ МИГРАЦИИ" -s .\GuitarCogApi\ -p .\GuitarCogData\ `

Для обновления базы данных:
1) перейти в корневую папку решения (папку с файлом GuitarCogBackend.sln)
2) `dotnet ef database update -s .\GuitarCogApi\ -p .\GuitarCogData\ `

## Путь до сваггера: `[HOST]/swagger/index.html`

## Аутентификация/Авторизация
Аутентификация с помощью JWT токенов, срок жизни - 30 минут<br>
Обновление токена - с помощью Refresh токена, хранится в бд в юзере<br>
Соответствующие эндпоинты по пути `[HOST]/Auth/*`