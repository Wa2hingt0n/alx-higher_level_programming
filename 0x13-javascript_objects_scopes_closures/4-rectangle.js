#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let end = '';
      for (let j = 0; j < this.width; j++) {
        end += 'X';
      }
      console.log(end);
    }
  }

  rotate () {
    const newWidth = this.height;
    const newHeight = this.width;
    this.width = newWidth;
    this.height = newHeight;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
