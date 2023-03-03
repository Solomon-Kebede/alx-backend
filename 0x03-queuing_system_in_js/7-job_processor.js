
const kue = require('kue')
const queue = kue.createQueue();
//const cluster = require('cluster');
//const clusterWorkerSize = 2;

//let blacklist = [4153518780, 4153518781];

queue.process('push_notification_code_2', (job, done) => {
  const data = job.data;
  const phoneNumber = data.phoneNumber;
  const message = data.message;
  // console.log(job.data);
  sendNotification(phoneNumber, message, job, done);
})

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  const blacklist = ['4153518780', '4153518781'];
  //console.log(typeof(phoneNumber));
  //console.log(`${phoneNumber}  -> ${blacklist.includes(phoneNumber)}`);
  const truthValue = blacklist.includes(phoneNumber);
  if (truthValue === true) {
  //if (phoneNumber == '4153518781' | phoneNumber == '4153518780') {
    // console.log(`Phone number ${phoneNumber} is blacklisted`);
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else if (!truthValue) {
  //else if (!blacklist.includes(phoneNumber)) {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}

