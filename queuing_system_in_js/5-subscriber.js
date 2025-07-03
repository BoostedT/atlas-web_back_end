// 5-subscriber.js
import { createClient } from 'redis';

const client = createClient();
const subscriber = client.duplicate();

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

(async () => {
  await client.connect();
  await subscriber.connect();

  await subscriber.subscribe('holberton school channel', async (message) => {
    if (message === 'KILL_SERVER') {
      await subscriber.unsubscribe('holberton school channel');
      await subscriber.quit();
      await client.quit();
    } else {
      console.log(message);
    }
  });
})();
