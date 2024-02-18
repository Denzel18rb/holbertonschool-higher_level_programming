// Wait for the document to be fully loaded
$(document).ready(() => {
  // When the div with id "toggle_header" is clicked,
  // toggle between the classes "red" and "green" on the header element using jQuery
  $('DIV#toggle_header').click(() => {
    const header = $('header');

    // Check if the header has the class "red"
    if (header.hasClass('red')) {
      // If it has, remove class "red" and add class "green"
      header.removeClass('red').addClass('green');
    } else {
      // If it doesn't have class "red", remove class "green" and add class "red"
      header.removeClass('green').addClass('red');
    }
  });
});
