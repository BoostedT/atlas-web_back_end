const fs = require('fs');

function countStudents(path) {
  try {
    console.log('Reading file:', path);
    const data = fs.readFileSync(path, 'utf8');

    console.log('Raw content:\n', data);
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    if (lines.length <= 1) {
      console.log('Error: Only header or empty file');
      throw new Error('Cannot load the database');
    }

    const students = {};
    let total = 0;

    lines.slice(1).forEach((line) => {
      const parts = line.split(',');
      if (parts.length < 4) {
        console.log('Skipping malformed line:', line);
        return;
      }

      const firstname = parts[0].trim();
      const field = parts[3].trim();

      if (!students[field]) {
        students[field] = [];
      }

      students[field].push(firstname);
      total++;
    });

    console.log(`Number of students: ${total}`);
    for (const field in students) {
      console.log(`Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`);
    }
  } catch (err) {
    console.error('Caught error:', err.message);
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
