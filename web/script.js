
//bind click on video name to play it
$('#playlist li').each(function(){
  $(this).click(function(){
    var curUrl = $(this).attr("src");
    $('#videoArea').attr("src",curUrl)
    $('#videoArea').attr("autoplay","autoplay")

    $('#playlist > li[active]').removeAttr('active');
    $(this).attr('active','');
  });
});

//function to play next video
function playVideo(next=1){
  var activeVideo = $("#playlist > li[src='"+$("#videoArea").attr("src")+"']")
  var video;
  if(next == 1){
    video = activeVideo.next();
  }
  else{
    video = activeVideo.prev();
  }
  if(video.length == 0)
  	return;

  $('#videoArea').attr("src", video.attr("src"))
  $('#videoArea').attr("autoplay","autoplay")

  video.attr('active','');
  activeVideo.removeAttr('active');
};

//resize playlist with video
// $('#videoArea').resize(function(){
//   $('#playlistContainer').height($('#videoArea').height());
// });

//resize player on page load
// $(function(){
//   $('#videoArea').width($('#videoContainer').width()*0.99);
// });

//play next video when current is ended
$("#videoArea").on('ended',function(){ playVideo(1); });


$(function(){
  $("#left svg").click(function(){
    playVideo(0)
  });
  $("#right svg").click(function(){
    playVideo(1)
  });
});
