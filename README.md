# deploy

## Guide
** Getting started **

First of all, node.js is needed. Follow the guide on https://www.youtube.com/watch?v=530FEFogfBQ to get started with the basics of Microsoft Bot Framework (MSB)
** bot & website interaction during development **

The bot exists in the rostbot folder (rostbot = Region Östergötland Bot). During development, the bot can be tested by using *Bot Emulator Framework*.
In the bot-site folder, the webpage where the bot will be accessed when deployed to Microsoft Azure is located. As it stands, there is no easy way to test the bot via this webpage locally. Therefore, the development of the website will be separated from the development of the bot's logic and behaviour. The website can simply be seen as a "container" for the bot client.