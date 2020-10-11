const directline = require('offline-directline');
const express = require('express');

const app = express();
directline.initializeRoutes(app, 3000, 'http://0.0.0.0:8080');

app.get("/",function(request, response){
    var id = request.params.id;

    response.writeHead(200, {"Content-Type": "application/json"});
    response.write(JSON.stringify('Hello'));
    console.log("someone accessed our site");
});