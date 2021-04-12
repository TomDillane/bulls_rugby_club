$(document).ready(function () {
    $('.sidenav').sidenav();
    $('select').formSelect();
});

function check() {
    let member = document.getElementById("member-selector").value;
    if(member == "player") {
        document.getElementById("position-select").style.display = 'block';
    document.getElementById("gender-select").style.display = 'block';
    document.getElementById("pos-selector").required = true;
    document.getElementById("gender-select").required = true;
    }
    else {
        document.getElementById("position-select").style.display = 'none';
    document.getElementById("gender-select").style.display = 'none';
    document.getElementById("pos-selector").required = false;
    document.getElementById("gender-select").required = false;
    }
}


/*
function noshowpos() {
    document.getElementById('position-select').style.display = 'none';
    document.getElementById('gender-select').style.display = 'none';
}
function showpos() {
    document.getElementById('position-select').style.display = 'block';
    document.getElementById('gender-select').style.display = 'block';
}



$('#member-selector').change(function () {
    if(this.checked) {
        $('#gender-selector').prop('required', true);
        $('#pos-selector').prop('required', true);
    } else {
        $('#gender-selector').prop('required', false);
        $('#pos-selector').prop('required', false);
    }
});
*/