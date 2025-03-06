export default function taskBlock(trueOrFalse) {
    task = false;
    task2 = true;
  
    if (trueOrFalse) {
      const task = true;
      const task2 = false;
    }
  
    return [task, task2];
  }
  