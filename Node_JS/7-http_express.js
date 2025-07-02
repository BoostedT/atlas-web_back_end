// 7-http_express.js
const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const database = process.argv[2];

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.set('Content-Type', 'text/plain');
  let response = 'This is the list of our students';

  try {
    const studentReport = await countStudents(database);
    response += `\n${studentReport}`;
    res.send(response);
  } catch (error) {
    res.send(`${response}\nCannot load the database`);
  }
});

app.listen(1245);

module.exports = app;
