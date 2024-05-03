$(document).ready(function() {
  // Attach a click event handler to the DIV#toggle_header element
  $("DIV#toggle_header").click(function() {
    // Toggle between classes "red" and "green" on the <header> element
    $("header").toggleClass("red green");
  });

