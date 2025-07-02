const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      try {
        const lines = data.split('\n').filter(line => line.trim() !== '');

        if (lines.length <= 1) {
          throw new Error('Cannot load the database');
        }

        const students = {};
        let total = 0;

        lines.slice(1).forEach(line => {
          const parts = line.split(',');
          if (parts.length < 4) return;

          const firstname = parts[0].trim();
          const field = parts[3].trim();

          if (!students[field]) {
            students[field] = [];
          }

          students[field].push(firstname);
          total++;
        });

        let output = `Number of students: ${total}`;
        for (const field in students) {
          output += `\nNumber of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`;
        }

        resolve(output); // ✅ return output instead of just logging
      } catch (e) {
        reject(new Error('Cannot load the database'));
      }
    });
  });
}

module.exports = countStudents;
