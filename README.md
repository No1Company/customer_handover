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

**For getting HTTP Request Functionality** 

If you don't have a branch, and want to get going, no worries, just create a branch from develop and you'll be set (for now, further instructions follow). 
	
If you do have a branch, and wish to implement the functionality, you can create a merge request from "http-request-functionality", that is available as a branch. Please do not squash the branch, as it then can be used by others (it's not the end of the world, if it were to happen, as it's simply a branch from develop). For this, you can set the "code approval" to 0, so you won't need to have approval for the merge. If it mentions merge conflicts. You'll have to resolve them locally, go to your main branch, then run git merge http-request-functionality (might have to run git fetch origin before). 

You should now have a folder called "backend" in the deploy folder. This folder contains a readme for setting up a virtual environment with python, doesn't take long. Follow these steps and you'll have the contents of file init.py hosted locally / on localhost. 

This enables the functionality to access the stored data through a "Send a HTTP Request" in Composer. You'll have to set the url to http://localhost:5000/available-times , give a result property (for example dialog.result), and write application/json in the content type input field. 
	
This HTTP request will result in (in my example) a variable dialog.result, which stores all data on the localhost. To access the statuscode for errorhandling, one could write an if statement: if dialog.result.statusCode == 200, the statusCode will be 200 on success. 
	
To get something useful from this variable, you can write dialog.result.content[0].start (surrounded with ${placeholder} in some cases. This would return the starting time for the date with index 0 in the JSON file which is on the localhost. The 0 could of course be changed all the way up to 4, where the limit of the available data is.