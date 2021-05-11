// materialize initialization 
$(document).ready(function () {
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.datepicker').datepicker();
});

// condition on signup form to show player relevant fields if player selected

function playercheck() {
    let member = document.getElementById("member-selector").value;
    if (member == "player") {
        document.getElementById("position-select").style.display = 'block';
        document.getElementById("gender-select").style.display = 'block';
        document.getElementById("image-url-wrap").style.display = 'block';
        document.getElementById("pos-selector").required = true;
        document.getElementById("gender-selector").required = true;
        document.getElementById("image-url").required = true;
    }
    else {
        document.getElementById("position-select").style.display = 'none';
        document.getElementById("gender-select").style.display = 'none';
        document.getElementById("image-url-wrap").style.display = 'none';
        document.getElementById("pos-selector").required = false;
        document.getElementById("gender-selector").required = false;
        document.getElementById("image-url").required = false;
    }
}

// condition on signup form to show player meet point if player opts in as available for game
function check1() {
    let avail = document.getElementById("avail-selector").value;
    if (avail == "available") {
        document.getElementById("meet-select").style.display = 'block';
        document.getElementById("meet-selector").required = true;
    } else {
        document.getElementById("meet-select").style.display = 'none';
        document.getElementById("meet-selector").required = false;
    }
}

