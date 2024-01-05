#!/usr/bin/node
/**
 * File write Script
 *
 * This script write the content of a file specified as a command-line argument.
 * It uses the Node.js fs module to read the file asynchronously.
 */

/* Get the file path from the command-line arguments */
const filePath = process.argv[2];
const content = process.argv[3];
const fs = require('fs');

/*  Check if a file path is provided */
if (!filePath) {
  console.error('Specify the file path');
  process.exit(1);
}

/*  write iny the file content asynchronously */
fs.writeFile(filePath, content, 'utf-8', (error) => {
  /* Print the content or an error message */
  if (error) {
    console.log(error);
  }
});
