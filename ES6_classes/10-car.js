export default class Car {
  constructor(brand, motor, color) {
    if (typeof brand!== 'string' || typeof motor!== 'string' || typeof color!== 'string') throw Error('All attributes must be strings');

    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const NewObj = this.constructor[Symbol.species] || this.constructor;
    const clone = new NewObj();
    return clone;
  }
}
