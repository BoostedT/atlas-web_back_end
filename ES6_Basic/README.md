# ES6 Basics 📜

## Overview
This project covers fundamental **ES6 features** like `const`, `let`, and modular functions.

## Code Example
```javascript
export function taskFirst() {
  const task = 'I prefer const when I can.';
  return task;
}

export function getLastPhrase() {
  return ' is okay';
}

export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLastPhrase();
  return combination;
}
