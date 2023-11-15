#!/usr/bin/node

// Function to compute factorial recursively
function factorial (n) {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  }

  // Base case: factorial of 0 is 1
  if (n === 0) {
    return 1;
  }

  // Recursive case: n! = n * (n-1)!
  return n * factorial(n - 1);
}

// Get the input from the command line argument
const arg = process.argv[2];

// Compute and print the factorial
console.log(factorial(parseInt(arg)));
