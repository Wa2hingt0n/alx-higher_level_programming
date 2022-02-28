#!/usr/bin/node

function factorial (num) {
  if (isNaN(num) || num === 0 || num === 1) {
    return (1);
  }

  return (num * factorial(num - 1));
}

const result = factorial(parseInt(process.argv[2]));
console.log(result);
