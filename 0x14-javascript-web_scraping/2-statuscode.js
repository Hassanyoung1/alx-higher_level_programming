#!/usr/bin/env node
/**
 * File Write Script
 *
 * This script writes the HTTP status code of a specified URL provided as a command-line argument.
 * It uses the Node.js 'request' module to make an HTTP GET request.
 */

/* Get the URL from the command-line arguments */
const request = require("request");
const url = process.argv[2];

/* Check if a URL is provided */
if (!url) {
  console.error('Specify the URL');
  process.exit(1);
}

/* Make an HTTP GET request to the specified URL */
request(url, function (error, response) {
/*  Check for errors and log the HTTP status code */
  if (error) {
    console.error(`Error: ${error.message}`);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
