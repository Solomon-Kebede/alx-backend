const kue = require('kue')
let queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  //console.log(Array.isArray(jobs));
  if (!Array.isArray(jobs)) {
    throw new Error("Jobs is not an array");
  }
  jobs.forEach((value) => {
    // console.log(value);
    let job = queue.create('push_notification_code_3', value).save((err) => {
       if(err) {
        console.log(`Notification job ${job.id} failed: ${err}`);
      } else if (!err) {
        console.log(`Notification job created: ${job.id}`)
      }
    });

    job.on('complete', function(result){
      console.log(`Notification job ${job.id} completed`);
    }).on('failed', function(errorMessage){
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    }).on('progress', function(percentage, data){
      // console.log('\r  job #' + job.id + ' ' + progress + '% complete with data ', data );
      console.log(`Notification job ${job.id} ${percentage}% complete`)
    });
  });
};

module.exports = createPushNotificationsJobs;
