#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < content.results.length; i++) {
      for (let j = 0; j < content.results[i].characters.length; j++) {
        if (content.results[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
