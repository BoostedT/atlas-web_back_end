import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('validates which jobs are inside the queue', () => {
    const jobs = [{ phoneNumber: '1234567890', message: 'Hello' }];
    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(1);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
  });
});
