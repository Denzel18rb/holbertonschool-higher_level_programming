// Wait for the document to be fully loaded
$(document).ready(() => {
  // Send a GET request to the SWAPI API to retrieve information about a character
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data) => {
    // Extract the name data from the response
    const element = data.name; // Get name data

    // Display the name data on the screen in the div with id "character"
    $('DIV#character').text(element); // Show data name on screen
  })
    // If there is an error, log the error message to the console
    .catch((error) => {
      console.error('Error:', error);
    });
});
