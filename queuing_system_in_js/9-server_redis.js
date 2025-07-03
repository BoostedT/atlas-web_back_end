import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);

/**
 * Sets the reserved stock for a given item ID.
 * @param {number} itemId
 * @param {number} stock
 */
function reserveStockById(itemId, stock) {
  const key = `item.${itemId}`;
  client.set(key, stock);
}

/**
 * Gets the current reserved stock for a given item ID.
 * @param {number} itemId
 * @returns {Promise<string|null>} 
 */
async function getCurrentReservedStockById(itemId) {
  const key = `item.${itemId}`;
  const stock = await getAsync(key);
  return stock;
}

export {
  client,
  reserveStockById,
  getCurrentReservedStockById
};
