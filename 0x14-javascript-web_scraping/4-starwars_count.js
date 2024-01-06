#!/usr/bin/node
/**
 * This script queries the Star Wars API (https://swapi-api.alx-tools.com/api/films/)
 * and prints the number of movies in which the character “Wedge Antilles” is present.
 */

const request = require('request');

/* Check if the API URL is provided as a command-line argument */
const url = process.argv[2];
if (!url) {
  console.error('Please provide API URL of the Star Wars API: https://swapi-api.alx-tools.com/api/films/');
  process.exit(1);
}

/* Make a request to the provided API URL */
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  /* Parse the response body to extract film data */
  const films = JSON.parse(body).results;
  let count = 0;

  /* Iterate through each film and its characters to count occurrences of "Wedge Antilles" */
  for (const film of films) {
    for (const character of film.characters) {
      if (character.endsWith('/18/')) {
        count++;
      }
    }
  }

  /* Print the total number of movies featuring "Wedge Antilles" */
  console.log(count);
});
