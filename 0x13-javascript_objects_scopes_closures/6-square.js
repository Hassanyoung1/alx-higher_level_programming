#!/usr/bin/node
/*
*a class Square that defines
*a square and inherits from Rectangle of 4-rectangle.js
*/

const DupSquare = require('./5-square');

class Square extends DupSquare {
  constructor (size) {
    super(size, size);
  }

  // an instance method called charPrint(c) that prints the rectangle using the character c
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += c;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
