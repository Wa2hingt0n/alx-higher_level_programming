#!/usr/bin/node
const myInteger = parseInt(process.argv[2], 10);
if (isNaN(myInteger)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myInteger);
}
