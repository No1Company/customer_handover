FROM microsoft/dotnet

WORKDIR usr/src/app

COPY . .

WORKDIR /rostbot/runtime/azurewebapp

COPY . .

RUN dotnet build

EXPOSE 3979

CMD dotnet run

