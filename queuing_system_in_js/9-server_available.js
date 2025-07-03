import express from 'express';
import { listProducts } from './9-server_utils.js';
import { getCurrentReservedStockById } from './9-server_redis.js';

const app = express();
const port = 1245;

function getItemById(id) {
  return listProducts.find(item => item.id === id);
}

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const reserved = await getCurrentReservedStockById(itemId);
  const currentQuantity = item.stock - (parseInt(reserved) || 0);

  return res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: currentQuantity
  });
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});
