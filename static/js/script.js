$(document).ready(function () {
    $('.sidenav').sidenav();
    $('select').formSelect();
});


function noshowpos() {
    document.getElementById('position-select').style.display = 'none';
    document.getElementById('gender-select').style.display = 'none';
}
function showpos() {
    document.getElementById('position-select').style.display = 'block';
    document.getElementById('gender-select').style.display = 'block';
}

$('#player').change(function () {
    if(this.checked) {
        $('#male').prop('required', true);
        $('#pos-selector').prop('required', true);
    } else {
        $('#male').prop('required', false);
        $('#pos-selector').prop('required', false);
    }
});
