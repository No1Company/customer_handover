FROM microsoft/dotnet

WORKDIR usr/src/app

COPY . .

WORKDIR /rostbot/runtime/azurewebapp

COPY . .

RUN dotnet build Microsoft.BotFramework.Composer.WebApp.csproj

EXPOSE 3979

CMD dotnet run Microsoft.BotFramework.Composer.WebApp.csproj

