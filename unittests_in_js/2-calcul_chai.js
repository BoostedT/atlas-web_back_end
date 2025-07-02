// 2-calcul_chai.js
function calculateNumber(type, a, b) {
  const aRounded = Math.round(a);
  const bRounded = Math.round(b);

  switch (type) {
    case 'SUM':
      return aRounded + bRounded;
    case 'SUBTRACT':
      return aRounded - bRounded;
    case 'DIVIDE':
      return bRounded === 0 ? 'Error' : aRounded / bRounded;
    default:
      throw new Error('Invalid operation type');
  }
}

module.exports = calculateNumber;
