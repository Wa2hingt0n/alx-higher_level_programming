#!/usr/bin/node
const SquarePrev = require('./5-square');

class Square extends SquarePrev {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let end = '';
      for (let j = 0; j < this.width; j++) {
        end += c;
      }
      console.log(end);
    }
  }
}

module.exports = Square;
