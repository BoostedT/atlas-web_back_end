// 9-api/api.test.js
const chai = require('chai');
const request = require('request');
const expect = chai.expect;

describe('Index page', () => {
  const url = 'http://localhost:7865';

  it('should return status code 200', (done) => {
    request.get(url, (err, res) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should return correct response body', (done) => {
    request.get(url, (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', () => {
  const base = 'http://localhost:7865/cart';

  it('should return 200 and correct message when ID is a number', (done) => {
    request.get(`${base}/12`, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return 404 when ID is NOT a number', (done) => {
    request.get(`${base}/hello`, (err, res) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });

  it('should return 404 for ID with special characters', (done) => {
    request.get(`${base}/12abc`, (err, res) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
