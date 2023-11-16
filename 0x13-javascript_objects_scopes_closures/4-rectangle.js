#!/usr/bin/node

/**
 * An empty class Rectangle that defines a rectangle.
 * You must use the class notation for defining your class.
 * Run the main test.
 */
class Rectangle {
  /**
   * Export class rectangle.
   */
  constructor(w, h) {
    /**
     * Defining class constructor.
     * width: Initialize the instance attribute width with the value of w.
     * height: Initialize the instance attribute height with the value of h.
     */
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate() {
      
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }


  double() {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;

