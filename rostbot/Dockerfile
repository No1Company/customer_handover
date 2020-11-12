FROM microsoft/dotnet

WORKDIR usr/src/app

COPY . .

WORKDIR /rostbot/runtime

RUN dotnet build

EXPOSE 3979

WORKDIR /azurewebapp

CMD dotnet run

COPY . .