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
// var i=0;
$('.dropdown').hover(function() {
  // console.log('hover');
  $(this).children('.dropdown-toggle').dropdown("toggle");
})
$("#qq-tools-show").click(function(){
    $('#qq-tools').animate({right:'0'});
    $('#qq-tools-show').hide();
    $('#qq-tools-hide').show();
});
 $("#qq-tools-hide").click(function(){
    $('#qq-tools').animate({right:'-150px'});
    $('#qq-tools-show').show();
    $('#qq-tools-hide').hide();
 });
for(var i=0;i<online.length;i++){
    if(online[i]==1){
        $('.qq-rides-cs ul li:eq('+i+')').find('img').attr('src','/static/image/qqonline.png');;
    }else {
        $('.qq-rides-cs li:eq('+i+')').find('img').attr('src','/static/image/qqoffline.png');
    }
}
})(jQuery);
