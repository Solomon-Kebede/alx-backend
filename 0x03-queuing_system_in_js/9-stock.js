// import express
const express = require('express');
// create an express app
const app = express();

// import redis
const redis = require('redis');

// import util
const util = require('util');

// create a client to connect to redis server
const client = redis.createClient();

// connect to redis server
client.on('connect', () => {
  console.log("Connected to Redis server");
});

// Create the following array
const listProducts = [
  {id: 1, name: "Suitcase 250", price: 50, stock: 4},
  {id: 2, name: "Suitcase 450", price: 100, stock: 10},
  {id: 3, name: "Suitcase 650", price: 350, stock: 2},
  {id: 4, name: "Suitcase 1050", price: 550, stock: 5}
]

// return item using id
function getItemById(id) {
  return listProducts[id - 1];
}

// Test function: getItemById
//console.log(getItemById(1));


function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock, redis.print);
}

// promisify client.get
client.get = util.promisify(client.get);

// getCurrentReservedStockById
async function getCurrentReservedStockById(itemId) {
  const value = await client.get(`item.${itemId}`);
  return value;
}

app.get('/list_products', (request, response) => {
  response.json(listProducts);
});


const PORT = 1245;
// express server listens on port
app.listen(PORT, () => {
  console.log(`Server listening on port: ${PORT}`);
});
