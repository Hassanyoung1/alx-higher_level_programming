#!/usr/bin/node

const request = require('request');

const url = 'https://swapi.dev/api/films/' + process.argv[2];
let chars = [];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const results = JSON.parse(body);
  chars = results.characters;
  getChars(0);
});

const getChars = (index) => {
  if (index === chars.length) {
    return;
  }

  request(chars[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const charresults = JSON.parse(body);
    console.log(charresults.name);
    getChars(index + 1);
  });
};
