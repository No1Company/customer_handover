FROM microsoft/dotnet

WORKDIR /usr/src/app

COPY . .

RUN dotnet build --project /runtime/azurewebapp

COPY . .

EXPOSE 3979

CMD dotnet run --project /runtime/azurewebapp

COPY . .