# Backend
Проекты в решении:
* GuitarCogApi - проект с ASP.NET API
* GuitarCogData - проект с ApplicationDbContext и сущностями

## Установка .NET и среды разработки
Для разработки рекомендуется использовать Rider или подходящую IDE, поддерживающую работу с C# и .NET.

Необходимо установить .NET SDK 7.

## Миграции
Connection String базы данных при разработке берется из файла appsettings.json.
При деплое сохранять продовую/стейджовую стрингу в переменных среды.

Для создания миграции:
1) перейти в корневую папку решения (папку с файлом GuitarCogBackend.sln)
2) dotnet ef migrations add "НАЗВАНИЕ МИГРАЦИИ" -s .\GuitarCogApi\ -p .\GuitarCogData\

Для обновления базы данных:
1) перейти в корневую папку решения (папку с файлом GuitarCogBackend.sln)
2) dotnet ef database update -s .\GuitarCogApi\ -p .\GuitarCogData\

## База данных Fly.io
WSL:
```
curl -L https://fly.io/install.sh | sh
```

Прописать пути, которые скрипт выпишет в конце установки, в моем случае:
```
export FLYCTL_INSTALL="/home/ravil/.fly"
export PATH="$FLYCTL_INSTALL/bin:$PATH"
```

```
fly auth login
```