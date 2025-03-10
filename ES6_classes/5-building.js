export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
  }

  evacuationWarningMessage() {
    return 'Class extending Building must override evacuationWarningMessage';
  }

  get sqft() {
    return this._sqft;
  }
}
