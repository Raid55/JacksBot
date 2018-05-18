$(document).ready(function () {
    $("#stopbtn").click(function() {
        if ($(this).hasClass("ui red green button")) {
            $.post("/dashboard", { status: "0" }, "json");
        } else {
            $.post("/dashboard", { status: "1" }, "json");
        }
        $('#stopmsg').text(function(i, text){
            return text == "Would you like to give the bot a rest?" ? "How about you start up the bot!" : "Would you like to give the bot a rest?";
        });
        $('#stopbtn').text(function(i, text){
            return text == "Stop!" ? "Start!" : "Stop!";
        });
        $("#stopbtn").toggleClass("red");
    });
});