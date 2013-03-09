(function() 
{
    var map = createMap();
    var userPos = addUser(map);
    $( document ).ready(function(){
        $('#searchbutton').click(function(){
            var bandname = $('#searchbox').val();
            function getPlaylist(){
                $.getJSON('/findartist/' + bandname + '/', function(data){
                    var minLatLng = [userPos];
                    console.log(userPos);
                    var maxLatLng = [userPos];
                    plotArtists(data, map, minLatLng, maxLatLng)});
            }
        var playlistRefresh = setInterval(getPlaylist, 5000);
	})
  	});
})();
