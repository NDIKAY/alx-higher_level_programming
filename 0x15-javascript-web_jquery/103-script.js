$(document).ready(function() {
  // Function to fetch translation
  function fetchTranslation() {
    var languageCode = $("#language_code").val();
    var apiUrl = "https://www.fourtonfish.com/hellosalut/hello/?lang=" + languageCode;

    $.getJSON(apiUrl, function(data) {
      $("#hello").text(data.hello);
    });
  }

  // Fetch translation when btn_translate is clicked
  $("#btn_translate").click(fetchTranslation);

  // Fetch translation when Enter key is pressed in language_code input
  $("#language_code").keypress(function(event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
