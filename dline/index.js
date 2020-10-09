const directline = require('offline-directline');
const express = require('express');

const app = express();
directline.initializeRoutes(app, 3000, 'http://0.0.0.0:8080');