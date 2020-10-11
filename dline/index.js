const directline = require('offline-directline');
const express = require('express');

const app = express();
directline.initializeRoutes = function(app, botUrl, conversationInitRequired = true) {
    directLineEndpoint = 'http://0.0.0.0:3000';
    const router = directline.getRouter(directLineEndpoint, botUrl, conversationInitRequired);
    app.use(router);
    app.listen(3000, () => {
        console.log("Custom init...");
        console.log('Listening for messages on ' + directLineEndpoint + '/directline');
        console.log('Routing messages to bot on ' + botUrl);
        
    });
}

app.get('/', function(req, res) {
    res.status(200).send("welcome!");
    console.log("någon anslöt");
});


directline.initializeRoutes(app, 'http://tddc88-company-1-2020.kubernetes-public.it.liu.se/api/messages', true);
