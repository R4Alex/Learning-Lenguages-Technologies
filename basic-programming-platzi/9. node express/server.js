var express = require('express');
var app = express();
 
app.get('/', function (req, res) {
    res.send('This is <strong>Home</strong>');
})

app.get('/curses', function(req, res){
    res.send('This is <strong>curses</strong>');
})

app.listen(8989);

