export default class Car {
  constructor(brand, motor, color) {
    if (typeof brand!== 'string' || typeof motor!== 'string' || typeof color!== 'string') throw Error('All attributes must be strings');

    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const cloneCar = this.constructor[Symbol.species] || this.constructor;
    return new cloneCar(this._brand, this._motor, this._color);
  }
}

Object.defineProperties(Car, Symbol.species, {
  get: function() {
    return this;
  }
});
