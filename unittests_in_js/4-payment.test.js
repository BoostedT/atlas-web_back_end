// 4-payment.test.js
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment'); // ✅ correct file
const { expect } = require('chai');

describe('sendPaymentRequestToApi', function () {
  it('should stub Utils.calculateNumber and log correct total', function () {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const consoleSpy = sinon.spy(console, 'log');
    sendPaymentRequestToApi(100, 20);
    expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
    stub.restore();
    consoleSpy.restore();
  });
});
