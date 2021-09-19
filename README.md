Net core 5 + Identity Server 4 (is4ef) + SqlServer
=========================

Add template: `dotnet new -i identityserver4.templates`

Create project: `dotnet new is4ef -n 'project_name'`

Update TargetFramework: `<TargetFramework>net5</TargetFramework>`

Update all nuget package.

Add nuget SqlServer: `Microsoft.EntityFrameworkCore.SqlServer`

Remove folder Migrations.

Add new Migrations:
1. `dotnet ef migrations add InitialIdentityServerConfigurationDbMigration -c ConfigurationDbContext -o Data/Migrations/ConfigurationDb`
2. `dotnet ef migrations add InitialIdentityServerPersistedGrantDbMigration -c PersistedGrantDbContext -o Data/Migrations/PersistedGrantDb`
3. Run `dotnet run /seed` or (`dotnet ef database update -c ConfigurationDbContext` and `dotnet ef database update -c PersistedGrantDbContext`)

Create scripts:
1. `dotnet ef migrations script -c ConfigurationDbContext -o Data/Migrations/Configuration`
2. `dotnet ef migrations script -c PersistedGrantDbContext -o Data/Migrations/PersistedGrant`

Register your IdentityServer with Google at: <https://console.developers.google.com>
Enable Google API
Set the redirect URI to `https://localhost:5001/signin-google`

Migrate user:
1. `dotnet ef migrations add InitialUser -c ApplicationDbContext -o Data/Migrations/UserDb`
2. `dotnet ef database update -c ApplicationDbContext`
