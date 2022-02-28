#!/usr/bin/node

const myIterator = parseInt(process.argv[2], 10);
if (isNaN(myIterator)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myIterator; i++) {
    console.log('C is fun');
  }
}
