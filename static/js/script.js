// materialize initialization 
$(document).ready(function () {
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.datepicker').datepicker();
});

// condition on signup form to show player relevant fields if selected
function check() {
    let member = document.getElementById("member-selector").value;
    if (member == "player")
     {
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
        document.getElementById("gender-select").style.display = 'none';
        document.getElementById("image-url-wrap").required = false;
        document.getElementById("gender-selector").required = false;
        document.getElementById("image-url").required = false;
    }
}
function check1() {
    let avail = document.getElementById("avail-selector").value;
    if (avail == "available")
    {
         document.getElementById("meet-select").style.display = 'block';
         document.getElementById("meet-selector").required = true;
    } else {
        document.getElementById("meet-select").style.display = 'none';
        document.getElementById("meet-selector").required = false;
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