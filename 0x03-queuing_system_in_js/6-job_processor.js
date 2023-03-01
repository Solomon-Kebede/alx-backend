const kue = require('kue')
let queue = kue.createQueue();

queue.process('push_notification_code', (job, done) => {
  const phoneNumber = job.data.phoneNumber;
  const message = job.data.message;
  console.log(job.data);
  sendNotification(phoneNumber, message);
  done();
})

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

