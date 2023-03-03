const kue = require('kue')
let queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  console.log(jobs);
  console.log(queue);
  return 0;
}

module.exports = createPushNotificationsJobs;
