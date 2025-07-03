// 4-redis_advanced_op.js
import pkg from 'redis';
const { createClient } = pkg;

const client = createClient({ legacyMode: true });

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.connect().then(() => {
  console.log('Redis client connected to the server');

  const key = 'HolbertonSchools';

  client.hset(key, 'Portland', 50, logReply);
  client.hset(key, 'Seattle', 80, logReply);
  client.hset(key, 'New York', 20, logReply);
  client.hset(key, 'Bogota', 20, logReply);
  client.hset(key, 'Cali', 40, logReply);
  client.hset(key, 'Paris', 2, logReply);

  client.hgetall(key, (err, reply) => {
    if (err) {
      console.error(`Error fetching hash: ${err.message}`);
      return;
    }
    console.log(reply);
  });
});

function logReply(err, reply) {
  if (err) {
    console.log(`Redis client not connected to the server: ${err.message}`);
  } else {
    console.log(`Reply: ${reply}`);
  }
}
