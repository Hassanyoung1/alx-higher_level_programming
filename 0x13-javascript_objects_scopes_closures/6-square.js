#!/usr/bin/node
/*
*a class Square that defines
*a square and inherits from Rectangle of 4-rectangle.js
*/

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
/* Create an instance method calledcharPrint(c) that printsthe rectangle using the character c */
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
