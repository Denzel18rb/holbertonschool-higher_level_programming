// Wait for the document to be fully loaded
$(document).ready(() => {
  // Send a GET request to the "https://hellosalut.stefanbohacek.dev/?lang=fr" endpoint
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    // Extract the value of the "hello" field from the response data
    const helloValue = data.hello;

    // Display the "hello" value on the screen in the div with id "hello"
    $('DIV#hello').text(helloValue); // Show data name on screen
  })
    // If there is an error during the request, log the error message to the console
    .fail((error) => {
      console.error('Error:', error);
    });
});
