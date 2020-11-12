FROM microsoft/dotnet

WORKDIR /usr/src/app

COPY . .

WORKDIR /rostbot/runtime/azurewebapp
RUN dotnet build

COPY . .

EXPOSE 3979

RUN dotnet run
