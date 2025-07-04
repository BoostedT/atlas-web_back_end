// 10-api/api.test.js
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

describe('/available_payments endpoint', () => {
  it('should return status 200 and correct JSON response', (done) => {
    request.get('http://localhost:7865/available_payments', { json: true }, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      });
      done();
    });
  });
});

describe('/login endpoint', () => {
  it('should return welcome message with valid userName', (done) => {
    request.post({
      url: 'http://localhost:7865/login',
      json: { userName: 'Tyler' }
    }, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(res.body).to.equal('Welcome Tyler');
      done();
    });
  });

  it('should return 400 if userName is missing', (done) => {
    request.post({
      url: 'http://localhost:7865/login',
      json: {}
    }, (err, res) => {
      expect(res.statusCode).to.equal(400);
      done();
    });
  });
});
