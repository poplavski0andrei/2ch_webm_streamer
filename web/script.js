

//saves info about video
function saveVideo(index){
    video = $('#videoArea')
    localStorage.setItem("activeVideo", index);
    volume = video.get(0).volume;
    console.log("saving volume " + volume)
    if(volume != undefined){
        volume = localStorage.setItem("volume", volume.toFixed(4));
    }
}

//bind click on video name to play it
$('#playlist li').each(function(){
  $(this).click(function(){
    var curUrl = $(this).attr("src");
    $('#videoArea').attr("src",curUrl)
    $('#videoArea').attr("autoplay","autoplay")

    $('#playlist > li[active]').removeAttr('active');
    $(this).attr('active','');
    //save active video to local storage
    saveVideo($(this).index());
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
  //save active Video to local storage
  saveVideo(video.index());
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

//load last played video
$(function(){
    var videoIndex = localStorage.getItem("activeVideo");
    var volume = localStorage.getItem("volume");
    if(videoIndex != undefined){
        var video = $('#playlist > li:nth-child(' + (parseInt(videoIndex) + 1) + ')')
        if(volume != "undefined"){
            $('#videoArea').get(0).volume = parseFloat(volume);
        }
        video.click();
        $('#videoArea').get(0).pause();
        $('#videoArea').get(0).muted = false;
    }
})
