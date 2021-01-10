console.log("main.js loaded")

$(document).ready(function() {
    $('.ui.dropdown')
        .dropdown();
});

$(document).ready(function() {
    $('.message .close')
      .on('click', function() {
        $(this).closest('.message').transition('fade')
        ;
      })
});