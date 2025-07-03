// 1-redis_op.js
import pkg from 'redis';
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

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error getting value for ${schoolName}: ${err.message}`);
      return;
    }
    console.log(reply);
  });
}
