# ROST-bot

## Guide
**Getting started**

First of all, node.js is needed. Follow the guide on https://www.youtube.com/watch?v=530FEFogfBQ to get started with the basics of Microsoft Bot Framework (MSB).

**Bot & website interaction during development**

The bot lies in the rostbot folder (rostbot = Region Östergötland Bot). During development, the bot can be tested by using *Bot Framework Emulator*.
In the bot-site folder, the webpage where the bot will be accessed when deployed to Microsoft Azure is located. As it stands, there is no easy way to test the bot via this webpage locally. Therefore, the development of the website will be separated from the development of the bot's logic and behaviour.

The website uses the Bot Framework WebChat component. More info can be found at https://github.com/microsoft/BotFramework-WebChat.

**Possible requirements to use `node index.js` for emulator testing**

If you run into the problem of not being able to run the command `node index.js` to test the bot with the emulator it might be because it requires dotenv and restify on line 11 and 13 in the index.js file. These do not seem to be included. While in the 'rostbot' folder run the command:

`npm install dotenv`

This will add the folder node_modules to the directory. This is a collection of modules commonly used. The `node index.js` command should now work and you can test with the emulator again. 

Do not forget to add the node_modules folder to .gitignore as it is not something we want to push.