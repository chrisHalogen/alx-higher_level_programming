$.get("https://swapi.co/api/people/5/?format=json", function (result) {
  $("DIV#character").text(result.name);
});
