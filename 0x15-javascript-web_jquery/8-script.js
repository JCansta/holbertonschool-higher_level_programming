// JS script that fetches ans list the title for all movies in an URL
$.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function({results}) {
    let movie;
    console.log(results);
    for (movie of results) {
        $("#list_movies").append(`<li>${movie["title"]}</li>`);
    }
});
