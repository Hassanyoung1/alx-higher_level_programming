#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const result = JSON.parse(body);
  const data = result.characters;

  for (const i of data) {
    request.get(i, function (error, response, body) {
      if (error) {
        console.log(error);
      }
      const data = JSON.parse(body);
      console.log(data.name);
    });
  }
});
