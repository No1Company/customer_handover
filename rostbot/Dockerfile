FROM microsoft/dotnet

WORKDIR usr/src/app

COPY . .

WORKDIR /rostbot/runtime

COPY . .

RUN dotnet build

EXPOSE 3979

WORKDIR /azurewebapp

COPY . .

CMD dotnet run

