$.get("https://swapi.co/api/films/?format=json", function (result) {
  $("UL#list_movies").append(
    ...result.results.map((movie) => `<li>${movie.title}</li>`)
  );
});
