// Wait for the document to be fully loaded
$(document).ready(() => {
  // When the div with id "red_header" is clicked,
  // change the text color of the header element to red using jQuery
  $('DIV#red_header').click(() => {
    $('header').css('color', 'red');
  });
});
