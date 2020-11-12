FROM microsoft/dotnet

WORKDIR usr/src/app

COPY . .

RUN dotnet build /rostbot/runtime/azurewebapp/Microsoft.BotFramework.Composer.WebApp.csproj

EXPOSE 3979

CMD dotnet run /rostbot/runtime/azurewebapp/Microsoft.BotFramework.Composer.WebApp.csproj

COPY . .