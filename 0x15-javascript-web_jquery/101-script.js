$(document).ready(function() {
  // Add item to the list when DIV#add_item is clicked
  $("#add_item").click(function() {
    $("ul.my_list").append("<li>Item</li>");
  });

  // Remove last item from the list when DIV#remove_item is clicked
  $("#remove_item").click(function() {
    $("ul.my_list li:last-child").remove();
  });

  // Clear the entire list when DIV#clear_list is clicked
  $("#clear_list").click(function() {
    $("ul.my_list").empty();
  });
});
