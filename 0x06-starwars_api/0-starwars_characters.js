#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as an argument');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, async (error, _response, body) => {
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

  // Use a for loop with await to fetch character names in order
  for (const characterUrl of characters) {
    try {
      const characterData = await fetchCharacter(characterUrl);
      console.log(characterData.name);
    } catch (err) {
      console.error('Error fetching character data:', err);
    }
  }
});

function fetchCharacter(url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, _response, body) => {
      if (error) {
        return reject(error);
      }
      const character = JSON.parse(body);
      resolve(character);
    });
  });
}
