#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const contents = JSON.parse(body);
    let done = {};
    contents.forEach((content) => {
      if (content.done && done[content.userId] === undefined) {
        done[content.userId] = 1;
      } else if (content.done) {
        done[content.userId] += 1;
      }
    });
    console.log(done);
  }
});
