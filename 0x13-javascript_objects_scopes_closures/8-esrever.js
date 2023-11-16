#!/usr/bin/node
/*
 * a function that returns the reversed version of a list:
 * @list: the list of array
*/
exports.esrever = function (list) {
  // Create an empty array to store the reversed elements
  const revList = [];
  // itirate
  for (let i = list.length - 1; i >= 0; i--) {
    // Add each element to the new reversed list
    revList.push(list[i]);
  }
  return revList;
};
