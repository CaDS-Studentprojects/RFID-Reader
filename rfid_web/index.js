var express = require('express');
var mqtt = require('mqtt');
var app = express();

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/bootstrap.html');
});

app.use("/js", express.static(__dirname + "/js"));
app.use("/css", express.static(__dirname + "/css"));
app.use("/img", express.static(__dirname + "/img"));

app.listen(3000, function () {
    console.log('RFID Reader listening on port 3000!');
});

var client  = mqtt.connect('tcp://etoPiBastelei:1883');

client.on('connect', function () {
    client.subscribe('rfid/#');
    console.log("Subscribed to all RFID topics");
});

client.on('message', function (topic, message) {
    console.log(message.toString());
});