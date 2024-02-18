// Wait for the document to be fully loaded
$(document).ready(() => {
  // When the div with id "add_item" is clicked,
  // append a new list item with text "Item" to the unordered list with class "my_list" using jQuery
  $('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>'); // Add to the list
  });
});
