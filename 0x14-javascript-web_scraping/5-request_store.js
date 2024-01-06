#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];
if (!url) {
  console.error('Please provide API URL of the Star Wars API: https://swapi-api.alx-tools.com/api/films/');
  process.exit(1);
}

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, { encoding: 'utf-8' }, function (error) {
      if (error) console.log(error);
    });
  }
});
