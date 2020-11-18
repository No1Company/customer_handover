# DotNet bot runtime

# Folder structure

* **core**: Includes all core JavaScript runtime logic, independent of hosting technology.
* **technology specific folders**: Each hosting technology has one folder in this directory. For example, for Azure Functions, there is an `azurefunction` folder

 - **tests**: Javascript runtime tests

-**Custom Actions Instructions**  
Man kan behöva köra dessa (men det är inte säkert att man behöver det, det kan vara för 
första setupen, återkoppla gärna), de går antagligen att köra i valfri mapp [TERMINAL]: 
(NYA STEG: 
    npm config set registry https://registry.npmjs.org/ (in composer doc, it asks you to set the registry to myget, which is out of date now.)
    bf plugins:uninstall @microsoft/bf-dialog (in composer doc, it ask you to install this plugin, which is also out of date now).
    npm i -g @microsoft/botframework-cli
    .\update-schema.ps1
    close composer and reopen it again.
)
npm config set registry https://botbuilder.myget.org/F/botframework-cli/npm/ 
npm i -g @microsoft/botframework-cli
bf plugins:install @microsoft/bf-dialog

I mappen rostbot\runtime\customaction\Action [EDITOR]:
Skapa en ny C#-fil ([NAMN PÅ KLASS].cs). Kopiera en av filerna i mappen, t.ex. "AddString.cs". 
Byt klassnamn, konstruktornamn och "public const string Kind =["NAMN PÅ KLASS"];
Ändra på funktionalitet i botten av filen för att göra egna funktioner. 

I filen rostbot\runtime\customaction\CustomActionComponentRegistration.cs [EDITOR]:
Lägg till yield return new DeclarativeType<[NAMN PÅ KLASS]>([NAMN PÅ KLASS].Kind);

I mappen rostbot\runtime\customaction\Schemas [EDITOR]:
Skapa en ny schemafil ([NAMN PÅ KLASS].schema) och byt ut "title": "[NAMN PÅ KLASS]", 

I mappen rostbot\runtime [TERMINAL]:
Här kan du köra dotnet build i terminalen så bör du få en rad text och eventuellt ett par varningsmeddelanden.
Här kan du också få något som liknar kompileringsfel, vilket underlättar felsökning vid syntax-fel. 

I mappen rostbot\schemas [TERMINAL]:
När detta är gjort kan du gå till mappen runtime och köra en powershell eller bashterminal, baserat på OS. 
Powershell kan startas i windows genom att skriva powershell i kommandotolken. 
Powershell: .\update-schema.ps1 -runtime azurewebapp 
Bash: sh ./update-schema.sh -runtime azurewebapp
(Composer kan inte vara öppen samtidigt som detta script körs)
Detta kommer ta din schemafil som du skrivit i customaction/schemas och lägga till den i schemafilen
för hela projektet, alltså deploy\rostbot\schemas\sdk.schema. 
För mig fungerade inte detta script i bash, men fungerade i Powershell, så ifall du kör linux kan
du behöva pusha till en git och be någon annan köra scriptet. 
Återkoppla gärna ifall det skulle fungera i bash så kan jag ta bort detta och försöka igen på ubuntu. 

I mappen rostbot\ [COMPOSER]:
Öppna composer, tryck på knapparna för att lägga till funktioner. Nu bör din funktion finnas under custom actions. 
Där kan du skriva in variabler som skickas in, och vilken variabel som ska ta emot svaret. För att skicka in variabler
behöver du använda "expression" (för siffror) och ${scope.string} för strängar (även ifall de skrivs i expressions). 
För siffror behöver du inte använda ${}, men det fungerar inte att använda variabler direkt i "integer-fältet". 

**Konfigurering (uppdateras):** 

I schemafiler rostbot\runtime\customaction\Schemas\*.schema:   
"arg2": {
    "$ref": "schema:#/definitions/integerExpression",
    "title": "Arg2",
    "description": "Value from callers memory to use as arg 2" .

Värdet "arg2" i början av json-objektet kopplas till C# filen genom [JsonProperty("arg2")] 
som ligger i C#-filen. Detta är följt av public NumberExpression Arg2 { get; set; }. 
Det sistnämnda uppfattar jag som ett sätt att göra Arg2 till en fil-lokal variabel med 
värdena som har skrivits in i arg2-fältet i composer. För att skapa nya variabler att ta in från Composer behöver man 
lägga till ett nytt fält i schemafilen, med ett nytt id ("arg2"), och ta emot den på identiskt sätt som övriga variabler i C# filen. 
Det är inte helt självklart hur man hämtar och sätter värden, men det kan undersökas genom att titta på exempel 
från de som finns för tillfället (de flesta är väldigt liknande i dagsläget). 

**Felsökning (uppdateras):**
Anledningen till att funktioner kan få "Object reference..." ligger mest antagligen i ett
problem med benämningen av funktionerna. Var konsekvent med namn på fil, klass, konstruktor, kind och registrering
(vid yield return new i rostbot\runtime\customaction\CustomActionComponentRegistration.cs). 

Det finns ett fel som lyder: Error Processing Schema
Definition not found for Microsoft.Ask/properties/activity/oneOf/1/properties/membersAdded/items
Jag har gjort ett inlägg på Composers forum och väntar på svar. Men tills vidare får det vara så. 
Det verkar inte påverka funktionaliteten av composer. 
