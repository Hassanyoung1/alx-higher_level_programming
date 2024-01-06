#!/usr/bin/node
/**
 * Wedge Antilles Movie Count Script
 *
 * This script fetches and prints the number of Star Wars movies where the character "Wedge Antilles" is present.
 * It uses the Node.js 'request' module to make an HTTP GET request to the Star Wars API.
 */

/* Import the 'request' module */
const request = require('request');

/* Get the API URL from the command-line arguments */
const apiUrl = process.argv[2];

/* Check if an API URL is provided */
if (!apiUrl) {
  console.error('Specify the Star Wars API URL');
  process.exit(1);
}

/* Character ID for Wedge Antilles */
const characterId = 18;

/* Make an HTTP GET request to the Star Wars API */
request(apiUrl, function (error, response, body) {
  /* Check for errors */
  if (error) {
    console.error(`Error: ${error.message}`);
  } else {
    /* Parse the JSON response */
    const filmsData = JSON.parse(body);

    /* Initialize a counter for movies with Wedge Antilles */
    let moviesWithWedgeCount = 0;

    /* Function to check if Wedge Antilles is present in a film */
    const isWedgePresent = (film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);

    /* Count movies with Wedge Antilles */
    filmsData.results.forEach((film) => {
      if (isWedgePresent(film)) {
        moviesWithWedgeCount++;
      }
    });

    /* Print the number of movies with Wedge Antilles */
    console.log(`${moviesWithWedgeCount}`);
  }
});
