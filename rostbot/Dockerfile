FROM microsoft/dotnet

WORKDIR /usr/src/app

COPY . .
RUN ls
WORKDIR /rostbot/runtime/core
RUN ls
RUN dotnet build 

COPY . .

EXPOSE 3979

RUN dotnet run /azurewebapp/Microsoft.BotFramework.Composer.WebApp.csproj
