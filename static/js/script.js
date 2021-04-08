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




