// 1-redis_op.js
import pkg from 'redis';
import { promisify } from 'util';
const { createClient } = pkg;
const print = pkg.print;

const client = createClient({ legacyMode: true });

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.connect().then(() => {
  console.log('Redis client connected to the server');

  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.log(`Redis client not connected to the server: ${err.message}`);
    } else {
      console.log(`Reply: ${reply}`);
    }
  });
}

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error getting value for ${schoolName}: ${err.message}`);
  }
}