FROM microsoft/dotnet

WORKDIR /usr/src/app

COPY . .

WORKDIR /rostbot/runtime/
RUN dotnet build /core/Microsoft.BotFramework.Composer.Core.csproj

COPY . .

EXPOSE 3979

RUN dotnet run /azurewebapp/Microsoft.BotFramework.Composer.WebApp.csproj
