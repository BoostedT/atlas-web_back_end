export default class HolbertonClass {
  constructor(size, location) {
    /* eslint-disable space-infix-ops */
    if (typeof size!== 'number') throw Error('Size must be a number');
    if (typeof location!== 'string') throw Error('Location must be a string');

    this._size = size;
    this._location = location;
  }

  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}
