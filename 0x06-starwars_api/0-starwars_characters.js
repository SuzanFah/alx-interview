#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const filmEndpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to get character name from URL
const getCharacterName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

// Main function to fetch and display characters
request(filmEndpoint, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  
  // Use Promise.all to maintain order of characters
  try {
    const names = await Promise.all(
      characters.map(url => getCharacterName(url))
    );
    names.forEach(name => console.log(name));
  } catch (err) {
    console.error(err);
  }
});
