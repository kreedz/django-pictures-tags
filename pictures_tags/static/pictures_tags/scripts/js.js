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
            $.get("add-tag", {tag: tag}, function(data){
                if (data.created) {
                    var clone_tag = $(".tag").last().clone(true, true).insertAfter("div.tag:last");
                    clone_tag.children("span.tag-name").text(tag);
                }
            });
        });
        $(".tag-delete").click(function(){
            var tag = $(this).prev().text().trim();
            var tag_delete = $(this).parent();
            $.get("delete-tag", {tag: tag}, function(data){
                if (data.deleted) {
                    tag_delete.remove();
                }
            });
        });
    }
});
