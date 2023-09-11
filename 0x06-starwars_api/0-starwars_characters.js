#!/usr/bin/node
const request = require('request');

const API_URL = 'https://swapi-api.hbtn.io/api';

async function getCharacterNames (movieId) {
  try {
    request(`${API_URL}/films/${movieId}/`, (err, _, body) => {
      if (err) {
        console.error(err.message);
        return;
      }
      const charactersURL = JSON.parse(body).characters;
      const characterPromises = charactersURL.map((url) => {
        return new Promise((resolve, reject) => {
          request(url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              reject(promiseErr);
            } else {
              resolve(JSON.parse(charactersReqBody).name);
            }
          });
        });
      });

      Promise.all(characterPromises)
        .then((names) => console.log(names.join('\n')))
        .catch((allErr) => console.error(allErr));
    });
  } catch (error) {
    console.error(error.message);
  }
}

if (process.argv.length <= 2) {
  console.error('Usage: node script.js <Movie_ID>');
  process.exit(1);
}

const movieId = process.argv[2];
getCharacterNames(movieId);
