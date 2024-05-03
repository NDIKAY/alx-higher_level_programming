$(document).ready(function() {
  // Use jQuery AJAX function to fetch data from the URL
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function(data) {
      // Iterate through the results and extract the movie titles
      data.results.forEach(function(movie) {
        // Append each movie title to the UL#list_movies element
        $("UL#list_movies").append("<li>" + movie.title + "</li>");
      });
    },
    error: function(xhr, status, error) {
      // Handle error if any
      console.error('Error:', error);
    }
  });
});
