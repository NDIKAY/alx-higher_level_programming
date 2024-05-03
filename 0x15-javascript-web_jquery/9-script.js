$(document).ready(function() {
  // Use jQuery AJAX function to fetch data from the URL
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function(data) {
      // Update the content of DIV#hello with the translated greeting
      $("DIV#hello").text(data.hello);
    },
    error: function(xhr, status, error) {
      // Handle error if any
      console.error('Error:', error);
    }
  });
});
