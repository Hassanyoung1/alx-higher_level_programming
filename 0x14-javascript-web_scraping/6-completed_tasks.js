#!/usr/bin/node

/**
 * Script for Fetching Completed Tasks
 *
 * This script fetches completed tasks from a specified URL and displays the count
 * of completed tasks for each user.
 */

const request = require('request');

/** Get the URL from the command-line arguments */
const url = process.argv[2];

/** Check if a URL is provided */
if (!url) {
  console.error('Specify the URL');
  process.exit(1); /** Exit the script with an error status */
}

/** Make a request to the specified URL */
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    /** Parse the JSON response to obtain tasks */
    const tasks = JSON.parse(body);

    /** Count the completed tasks for each user */
    const completed = tasks.reduce((acc, task) => {
      if (task.completed === true) {
        acc[task.userId] = (acc[task.userId] || 0) + 1;
      }
      return acc;
    }, {});

    /** Display the count of completed tasks for each user */
    console.log(completed);
  }
});
