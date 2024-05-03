$(document).ready(function() {
  // Attach a click event handler to the DIV#update_header element
  $("DIV#update_header").click(function() {
    // Update the text content of the <header> element to "New Header!!!"
    $("header").text("New Header!!!");
  });
});
