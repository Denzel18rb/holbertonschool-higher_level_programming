// Wait for the document to be fully loaded
$(document).ready(() => {
  // When the div with id "red_header" is clicked,
  // add the class "red" to the header element using jQuery
  $('DIV#red_header').click(() => {
    $('header').addClass('red'); // Add class
  });
});
