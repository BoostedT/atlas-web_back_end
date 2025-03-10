export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  if (this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
    throw new Error("Class extending Building must override evacuationWarningMessage");
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
