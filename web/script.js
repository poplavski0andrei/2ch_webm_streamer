$('#playlist li').each(function(){
$(this).click(function(){
var curUrl =$(this).attr("src");
$('#videoarea').attr("src",curUrl)
$('#videoarea').attr("autoplay","autoplay")

$('#playlist > li[active]').removeAttr('active');
$(this).attr('active','');
});
});

function playNext(){
  var activeVideo = $("#playlist > li[src='"+$("#videoarea").attr("src")+"']")
  var video = activeVideo.next();
  if(video.length == 0)
  	return;

  $('#videoarea').attr("src", video.attr("src"))
  $('#videoarea').attr("autoplay","autoplay")

  video.attr('active','');
  activeVideo.removeAttr('active');
};

$(window).resize(function(){
  $('#videoarea').width($('#videoContainer').width()*0.99);
});

$(function(){
  $('#videoarea').width($('#videoContainer').width()*0.99);
});

$("#videoarea").on('ended',playNext)

