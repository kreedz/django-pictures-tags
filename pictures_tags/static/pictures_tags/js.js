$(document).ready(function(){
    $('input').click(function(){
        $.ajax({
            url: 'updatedb',
            type: 'get', //this is the default though, you don't actually need to always mention it
            success: function(data) {
                alert(data);
            },
            failure: function(data) { 
                alert('Got an error dude');
            }
        });
    });
});
