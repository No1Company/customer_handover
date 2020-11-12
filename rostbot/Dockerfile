FROM microsoft/dotnet

WORKDIR /usr/src/app

COPY . .

WORKDIR /rostbot/runtime/core
RUN dotnet build 

COPY . .

EXPOSE 3979

RUN dotnet run /azurewebapp/Microsoft.BotFramework.Composer.WebApp.csproj
