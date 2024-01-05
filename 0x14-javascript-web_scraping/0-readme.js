#!/usr/bin/env node
/**
 * File Reader Script
 *
 * This script reads the content of a file specified as a command-line argument.
 * It uses the Node.js fs module to read the file asynchronously.
 */

/* Get the file path from the command-line arguments */
const filePath = process.argv[2];
const fs = require('fs');

/*  Check if a file path is provided */
if (!filePath) {
  console.error('Specify the file path');
  process.exit(1);
}

/*  Read the file content asynchronously */
fs.readFile(filePath, 'utf-8', (error, content) => {
  /* Print the content or an error message */
  console.log(error || content);
});
