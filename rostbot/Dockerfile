FROM mcr.microsoft.com/dotnet/sdk:3.1
#FROM mcr.microsoft.com/dotnet/core/sdk:3.1.101
#FROM mcr.microsoft.com/dotnet/core/aspnet:3.1
#FROM mcr.microsoft.com/dotnet/core/sdk:3.1-bionic
WORKDIR /usr/src/app

COPY . .
RUN ls
WORKDIR /usr/src/app/runtime/azurewebapp
RUN dotnet build 

COPY . .

EXPOSE 3979

CMD ["dotnet", "run"]

COPY . .