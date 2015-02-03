$(document).ready(function(){
    if ($("body").data("title") === "options"){
        $("input").click(function(){
            $.ajax({
                url: "updatedb",
                type: "get",
                success: function(data){
                    alert(data);
                },
                failure: function(data){ 
                    alert("Got an error dude");
                }
            });
        });
    } else if ($("body").data("title") === "index"){
        $("input#add").click(function(){
            var tag = $("input[type='text']").val();
            $.ajax({
                url: "add-tag",
                type: "get",
                data: {tag: tag},
                success: function(data){
                    if (data.created) {
                        $("#tags").append($(".tag").last()
                                                   .clone()
                                                   .text(tag)
                                                   .insertAfter("div.tag:last"));
                    }
                },
                failure: function(data){ 
                    alert("Got an error dude");
                }
            });
        });
    }
});
