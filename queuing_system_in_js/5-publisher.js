// 5-publisher.js
import pkg from 'redis';
const { createClient } = pkg;

const client = createClient({ legacyMode: true });

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.connect().then(() => {
  function publishMessage(message, time) {
    setTimeout(() => {
      console.log(`About to send ${message}`);
      client.publish('holberton school channel', message);
    }, time);
  }

  publishMessage("Holberton Student #1 starts course", 100);
  publishMessage("Holberton Student #2 starts course", 200);
  publishMessage("KILL_SERVER", 300);
  publishMessage("Holberton Student #3 starts course", 400);
});
