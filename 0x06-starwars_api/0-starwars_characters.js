#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as an argument');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie');
    return;
  }

  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
