// JS script that fetche from an url an displays the value of hello
$(document).ready(function () {
    $.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", function({hello}) {
        $("#hello").text(hello);
    });
});
