$(document).ready(function() {
  // Attach a click event handler to the DIV#add_item element
  $("DIV#add_item").click(function() {
    // Append a new <li> element with text "Item" to the <ul> element with class "my_list"
    $("UL.my_list").append("<li>Item</li>");
  });
});
