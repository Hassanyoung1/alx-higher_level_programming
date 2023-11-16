#!/usr/bin/node
/**
 * An empty class Rectangle that define a rectangle
 * You must use the class notation for defining your class
 *i
 *run the main test
 *
 */

class Rectangle {
  /** export  class rectangle **/
  constructor (w, h) {
    /**
    *defining class constructor
    *width: Initialize the instance attribute width with the value of w
    *height: Initialize the instance attribute height with the value of h
    */
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
