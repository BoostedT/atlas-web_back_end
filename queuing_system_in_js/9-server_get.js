import express from 'express';
import { listProducts } from './9-server_utils.js';

const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  const formattedProducts = listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock
  }));
  res.json(formattedProducts);
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});
