const directline = require('offline-directline');
const express = require('express');

const app = express();
//app.listen(4000, '0.0.0.0'); //Make server listen on 0.0.0.0
directline.initializeRoutes(app, 'http://0.0.0.0:4000', 'http://0.0.0.0:8080', false);

app.get("/",function(request, response){
    var id = request.params.id;

    response.writeHead(200, {"Content-Type": "application/json"});
    response.write(JSON.stringify('Hello'));
    console.log("someone accessed our site");
});

console.log("directline rerouter created, listening on http://0.0.0.0:4000");