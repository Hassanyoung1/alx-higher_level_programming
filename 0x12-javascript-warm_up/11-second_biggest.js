#!/usr/bin/node

const findSecondLargest = (numbers) => {
  if (numbers.length < 2) {
    return 0;
  }

  numbers.sort((a, b) => b - a);
  return numbers[1];
};

const args = process.argv.slice(2).map(Number);

console.log(findSecondLargest(args));
