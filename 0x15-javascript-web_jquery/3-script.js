$(document).ready(function() {
  // Attach a click event handler to the DIV#red_header element
  $("DIV#red_header").click(function() {
    // Add the class "red" to the <header> element
    $("header").addClass("red");
  });
});

