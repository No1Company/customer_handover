FROM microsoft/dotnet

WORKDIR usr/src/app

COPY . .

RUN cd rostbot/runtime

RUN dotnet build

EXPOSE 3979

RUN cd azurewebapp

CMD dotnet run

COPY . .