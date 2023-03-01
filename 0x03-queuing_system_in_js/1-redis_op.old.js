import { createClient } from 'redis';
const client = createClient();
const redis = require('redis');

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  console.log(client.set(schoolName, value, redis.print))/*, (err, reply) => {
    if (err) {
      console.log('error 0: ', err);
    } else {
      console.log('Response: ', reply)
    }*/
  /*}));*/
}

function displaySchoolValue(schoolName) {
  console.log(client.get(schoolName, (err, obj) => {
    if (err) {
      console.log('error 0: ', err);
    } else {
      console.log('Retrieved OBJ: ', obj)
    }
  }));
}

/*
function setNewSchool(schoolName, value) {
  client.set(schoolName, value);
}

function displaySchoolValue(schoolName) {
  console.log(client.get(schoolName));
}
*/

/*
function setNewSchool(schoolName, value) {
  client.on('connect', () => {
    client.set(schoolName, value);
    console.log(`Key: ${schoolName} and value: ${value} set`);
  }); 
}

function displaySchoolValue(schoolName) {
  client.on('connect', () => {
    let value = client.get(schoolName);
    console.log(`Key: ${schoolName} and value: ${value} displayed`);
  }); 
}*/



displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
