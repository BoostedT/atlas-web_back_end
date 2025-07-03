// 0-redis_client.js
import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

async function run() {
  await client.connect();

  try {
    await client.set('Holberton', 'School');
    const value = await client.get('Holberton');
    console.log(`Value for Holberton: ${value}`);
  } catch (err) {
    console.error('Redis operation failed:', err);
  } finally {
    client.quit();
  }
}

run();
