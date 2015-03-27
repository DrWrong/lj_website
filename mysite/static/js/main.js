;(function($){
var height = $("#content").height();
$(".side_menu").css({
    "min-height": height + "px"
});
var height1 = $(".col-left .panel").height();
var height2 = $(".col-right .panel").height();
var height = height1>height2?height1:height2;
$(".col-left .panel").height(height);
$(".col-right .panel").height(height);
})(jQuery);
