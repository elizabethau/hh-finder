"use strict";

function showConfirmation(evt) {
    // prevents the browser from loading another page
    evt.preventDefault();

    // $.get('/details/<yelp_id>', (res) => {$('#ajax').html(res);});

    $('#ajacks').append('<p>Thanks!</p>');
}

$('#confirm').on('click', showConfirmation);
