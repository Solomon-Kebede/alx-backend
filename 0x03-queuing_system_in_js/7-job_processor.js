
 const kue = require('kue')
let queue = kue.createQueue();
let cluster = require('cluster');
let clusterWorkerSize = 2;

let blacklist = [4153518780, 4153518781];

queue.process('push_notification_code_2', (job, done) => {
  let data = job.data;
  let phoneNumber = data.phoneNumber;
  let message = data.message;
  // console.log(job.data);
  sendNotification(phoneNumber, message, job, done);
  done();
})

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklist.includes(phoneNumber)) {
    console.log(`Phone number ${phoneNumber} is blacklisted`);
    done();
  }
  else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}

