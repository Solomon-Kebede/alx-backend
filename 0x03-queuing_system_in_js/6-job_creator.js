const kue = require('kue')
let queue = kue.createQueue();

let job = queue.create('push_notification_code', {
  phoneNumber: '000-000-0000',
  message: 'Message to be sent',
}).save((err) => {
   if(err) {
    console.log('Notification job failed');
  } else if (!err) {
    console.log(`Notification job created: ${job.id}`)
  }
});

job.on('complete', (result) => {
  console.log('Job completed with data ', result);
});
