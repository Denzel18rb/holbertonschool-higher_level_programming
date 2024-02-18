// Wait for the document to be fully loaded
$(document).ready(() => {
  // Send a GET request to the SWAPI API to retrieve information about films
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
    // Extract the film data from the response
    const films = data.results; // Get data

    // Iterate through each film
    films.forEach((film) => {
      // Create a list item element and set its text to the film title
      const li = $('<li>').text(film.title); // Create element <li>

      // Append the list item to the unordered list with id "list_movies"
      $('#list_movies').append(li); // Add <li> to the list
    });
  })
    // If there is an error during the request, log the error message to the console
    .fail((error) => {
      console.error('Error:', error);
    });
});
