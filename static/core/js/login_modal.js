var $ = jQuery.noConflict();

function open_login(url) {
    $('#login').load(url, function (){
        $(this).modal('show');
    });
}