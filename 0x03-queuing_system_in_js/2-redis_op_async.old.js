import { createClient } from 'redis';
const client = createClient();
const redis = require('redis');
const util = require('util');

//const client.get = util.promisify(client.get);//.bind(client);

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.get = util.promisify(client.get);//.bind(client);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const value = await client.get(schoolName);
  console.log(value);
};

displaySchoolValue('Holberton')/*.then((value) => {
  console.log(value);
});*/
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
