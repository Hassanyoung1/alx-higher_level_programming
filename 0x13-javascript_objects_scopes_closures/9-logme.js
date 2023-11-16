#!/usr/bin/node

/*
 * a function that prints the number of arguments
 * already printed and the new argument value.
*/
// declare global variable
let count = 0;

// declare function
exports.logMe = function (item) {
  // print
  console.log(`${count}: ${item}`);
  // loop
  count++;
};
