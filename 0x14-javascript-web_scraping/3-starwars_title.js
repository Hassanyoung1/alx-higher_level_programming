#!/usr/bin/node
/**
 * Star Wars Movie Title Script
 *
 * This script fetches and prints the title of a Star Wars movie based on the episode number.
 * It uses the Node.js 'request' module to make an HTTP GET request to the Star Wars API.
 */

/* Import the 'request' module */
const request = require('request');

/* Get the movie ID from the command-line arguments */
const movieId = process.argv[2];

/* Check if a movie ID is provided */
if (!movieId) {
  console.error('Specify the movie ID');
  process.exit(1);
}

/* Star Wars API endpoint URL */
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

/* Make an HTTP GET request to the Star Wars API */
request(apiUrl, function (error, response, body) {
  /* Check for errors */
  if (error) {
    console.error(`Error: ${error.message}`);
  } else {
    /* Parse the JSON response */
    const movieData = JSON.parse(body);

    /* Check if the movie title is available */
    if (movieData.title) {
      console.log(`${movieData.title}`);
    } else {
      console.log(`No movie found with Episode ${movieId}`);
    }
  }
});
