//import { createClient } from 'redis';

// const client = createClient();
/*
client.on('error', err => console.log('Redis Client Error', err));

await client.connect();

await client.set('key', 'value');
const value = await client.get('key');
await client.disconnect();
*/
/*
const test = async function (err) {
  const client = createClient();
  client.on('error', err => console.log('Redis Client Error', err));
  await client.connect();
  await client.set('key', 'value');
  const value = await client.get('key');
  await client.disconnect();
}

test()
*/

import { createClient } from 'redis';
const client = createClient();

client.on('error', (err) => {
	console.log('Redis Client Error', err)
});

client.on('connect', () => {
	console.log('connected');
})
