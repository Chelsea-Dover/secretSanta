/**
 * Created by Chelsea on 12/5/15.
 */

var peopleId = [];
var groupNum = [];

function sendAjax() {
    $.ajax({
        url: '/exchange/' + groupNum + '/addsanta/', // the endpoint
        method: "POST", // http method
        data: {'peopleId':peopleId, 'groupNum':groupNum},
        success: function (json) {
            //$('#post-form').val(''); // remove the value from the input
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            console.log(errmsg, err);
        }
    });
}

function sendupdateajax(text, secondPart) {
    $.ajax({
        url: '/profile/' + idFromUrl + '/' + secondPart + '/', // the endpoint
        method: "POST", // http method
        data: {'idFormUrl':idFromUrl, 'text':text},
        success: function (json) {
            //$('#post-form').val(''); // remove the value from the input
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            console.log(errmsg, err);
        }
    });
}

function getNumber() {
    $(' .groupNum ').each(function () {
        $(this).find('p:gt(0)').each(function () {
            var idNumber = $(this).attr('id');
            groupNum.push(parseInt(idNumber));
        });

    });
}

function createpeople() {
    $(' .people ').each(function () {

        $(this).find('li').each(function () {
            var idNumber = $(this).attr('class');
            peopleId.push(parseInt(idNumber));
        });

    });
}

$('#post-assign').on('submit', function (event) {
    event.preventDefault();
    console.log("Selling form submitted! Let's see if it goes through");  // sanity check
    createpeople();
    console.log(peopleId);
    getNumber();
    console.log(groupNum);
    sendAjax();
});

$(' #editAddress ').on('submit', function(event) {
    event.preventDefault();
    var text = $(' #address ').val();
    var secondPart = "updateadress";
    console.log("Selling form submitted! Let's see if it goes through");  // sanity check
    sendupdateajax(text, secondPart);
    console.log(text);
});



$(' #editDislikes ').on('submit', function(event) {
    event.preventDefault();
    var text = $(' #dislikes ').val();
    var secondPart = "updatedislike";
    console.log("Selling form submitted! Let's see if it goes through");  // sanity check
    sendupdateajax(text, secondPart);
    console.log(text);
});


$(' #editLikes ').on('submit', function(event) {
    event.preventDefault();
    var text = $(' #likes ').val();
    var secondPart = "updateprofile";
    console.log("Selling form submitted! Let's see if it goes through");  // sanity check
    sendupdateajax(text, secondPart);
    console.log(text);
});


$(' .likesButton ').click(function(event){
    $(' .editlikeWrapper ').toggleClass(' edit ');
    $(' #likeId ').removeClass(' editLikeWrapper  ');
    $(' .dislikes ').addClass(' dontShow ')
});


$(' .dislikeButton ').click(function(event){
    $(' .editDislikeWrapper ').toggleClass(' edit ');
    $(' #dislikeId ').removeClass(' editDislikeWrapper  ');
    $(' .dislikes ').addClass(' dontShow ')
});

$(' .infoButton ').click(function(event){
    event.stopPropagation();
    $(' .editAddressWrapper ').toggleClass(' edit ');
    $(' #infoId ').removeClass(' editAddressWrapper  ');
    $(' .dislikes ').addClass(' dontShow ')
});