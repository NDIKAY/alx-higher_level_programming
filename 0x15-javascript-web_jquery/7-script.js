$(document).ready(function() {
  // Use jQuery AJAX function to fetch data from the URL
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function(data) {
      // Update the content of DIV#character with the character name
      $("DIV#character").text(data.name);
    },
    error: function(xhr, status, error) {
      // Handle error if any
      console.error('Error:', error);
    }
  });
});
