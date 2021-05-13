// JS scipt that fetches the character name from an url
$.getJSON("https://swapi-api.hbtn.io/api/people/5/?format=json", function({name}) {
    $("#character").text(name);
});
