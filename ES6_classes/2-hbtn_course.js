export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    if (!Array.isArray(students)) {
      throw new TypeError('Students must be an array');
    }
    if (students.every((student) => typeof student !== 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this.name = name
    this.length = length
    this.students = students
  }

  get name() {
    return this._name
  }
  set name(newnName) {
    if (typeof newnName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newnName
  }
  get length() {
    return this._length
  }
  set length(newLength) {