const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('should return 6 for SUM of 1.4 and 4.5', function () {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
    it('should return 5 for SUM of 1.2 and 3.7', function () {
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -4 for SUBTRACT of 1.4 and 4.5', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
    it('should return -3 for SUBTRACT of 3 and 5.4', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 3, 5.4), -2);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.2 for DIVIDE of 1.4 and 4.5', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
    it('should return "Error" for DIVIDE of 1.4 and 0', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
  });
});
