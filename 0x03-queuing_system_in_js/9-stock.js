// import express
const express = require('express');
// create an express app
const app = express();

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


app.get('/list_products', (request, response) => {
  response.json(listProducts);
});


const PORT = 1245;
// express server listens on port
app.listen(PORT, () => {
  console.log(`Server listening on port: ${PORT}`);
});
