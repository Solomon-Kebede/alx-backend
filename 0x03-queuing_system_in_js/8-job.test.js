// Import expectr from chai
const chai = require('chai');
const expect = chai.expect;
// import kue
const kue = require('kue');

// import createPushNotificationsJobs
import createPushNotificationsJobs from './8-job.js';

// Create a queue with kue
const queue = kue.createQueue();

// Make sure to enter test mode w/o processinng jobs

before(() => {
  queue.testMode.enter();
});


// Make sure to clear the queue and exit the test mode after executing tests

afterEach(() => {
  queue.testMode.clear();
});

after(() => {
  queue.testMode.exit();
});


// Writing tests
it('Test validates which jobs are inside the queue', () => {
  queue.createJob('job-1', {phoneNumber: '000-111-2222', message: 'I\'m job-1'}).save();
  queue.createJob('job-2', {phoneNumber: '333-444-5555', message: 'I\'m job-2'}).save();
  expect(queue.testMode.jobs.length).to.equal(2);
  expect(queue.testMode.jobs[0].type).to.equal('job-1');
  expect(queue.testMode.jobs[0].data).to.eql({phoneNumber: '000-111-2222', message: 'I\'m job-1'});
  expect(queue.testMode.jobs[1].type).to.equal('job-2');
  expect(queue.testMode.jobs[1].data).to.eql({phoneNumber: '333-444-5555', message: 'I\'m job-2'});
});
