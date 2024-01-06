#!/usr/bin/node
/**
 * Wedge Antilles Movie Count Script
 *
 * This script fetches and prints the number of Star Wars movies where the character "Wedge Antilles" is present.
 * It uses the Node.js 'request' module to make an HTTP GET request to the Star Wars API.
 */

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Specify the Star Wars API URL');
  process.exit(1);
}

const characterId = 18;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
    process.exit(1);
  }

  const filmsData = JSON.parse(body);
  let moviesWithWedgeCount = 0;

  const isWedgePresent = (film) =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);

  for (const film of filmsData.results) {
    if (isWedgePresent(film)) {
      moviesWithWedgeCount++;
    }
  }

  console.log(`${moviesWithWedgeCount}`);
});