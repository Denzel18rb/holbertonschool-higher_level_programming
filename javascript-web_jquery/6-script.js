// Wait for the document to be fully loaded
$(document).ready(() => {
  // When the div with id "update_header" is clicked,
  // change the text content of the header element to "New Header!!!" using jQuery
  $('DIV#update_header').click(() => {
    $('header').text('New Header!!!'); // Change text
  });
});
