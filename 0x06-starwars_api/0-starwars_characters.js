#!/usr/bin/node
const request = require('request');

const endpoint = 'https://swapi-api.hbtn.io/api';
const filmId = process.argv[2];

request(`${endpoint}/films/${filmId}/`, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const characters = JSON.parse(body).characters;

  // Use Promise.all to fetch all character names in parallel
  Promise.all(
    characters.map(
      (character) =>
        new Promise((resolve, reject) => {
          request(character, (error, response, body) => {
            if (error) reject(error);
            else resolve(JSON.parse(body).name);
          });
        })
    )
  )
    .then((names) => {
      names.forEach((name) => console.log(name));
    })
    .catch((error) => console.log(error));
});
