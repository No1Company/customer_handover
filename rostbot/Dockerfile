FROM mcr.microsoft.com/dotnet/sdk:3.1

WORKDIR /usr/src/app

COPY . .
WORKDIR /usr/src/app/runtime

RUN dotnet build 
COPY . .
EXPOSE 80
CMD dotnet run --project azurewebapp --urls http://localhost:80

COPY . .