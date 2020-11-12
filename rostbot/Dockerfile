FROM microsoft/dotnet

WORKDIR usr/src/app

COPY . .

EXPOSE 3979

RUN dotnet run --project rostbot/runtime/azurewebapp

COPY . .