
var client = require('aws-iot-device-sdk');
var fs = require('fs');

var conf = JSON.parse(fs.readFileSync('cert.json', 'utf8'));

var device = client.device({
  region: conf.region,
  clientId: conf.clientId,
  privateKey: conf.privateKey,
  clientCert: conf.clientCert,
  caCert: conf.caCert
});

device.on('connect', function() {
  console.log('connected.');
  device.publish(conf.topic, 'test message');
  console.log('published message.');
  return;
});
