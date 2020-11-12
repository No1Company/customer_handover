FROM microsoft/dotnet

WORKDIR /usr/src/app

COPY . .
RUN ls
WORKDIR /usr/src/app/runtime/azurewebapp
RUN dotnet build 

COPY . .

EXPOSE 3979

RUN dotnet run