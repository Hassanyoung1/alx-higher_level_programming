#!/usr/bin/node
/*
 *a function that converts a number from base 10 to another base passed as argument
 *@base : the base to be convetrd to
 */

exports.converter = function (base) {
// return function number
  return function (number) {
    // convert using tostring
    return number.toString(base);
  };
};
