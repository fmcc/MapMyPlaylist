$( document ).ready(function() 
{
  $('#startButton').click(function()
  {
    var username = $('input').val();
    var latestArtist = "";

    function getPlaylist()
    {
              // BUG: returns current tune at first but then removes
  	 $.getJSON('/finduserplaylist/' + username + '/', function(data) 
      {
        var artists = "";
                // checks to see if most recent artist has changed
        if (data[0].name != latestArtist)
        {
          $.each(data, function() 
          { // displays artist names currently for display purposes
            var location = new L.LatLng(this.lat, this.long);
            var name = this.name;
            var image = this.image;
            var marker = new L.Marker(location, { title: name });
            map.addLayer(marker);
          });
          $('#artists').html(artists);
          latestArtist = data[0].name;
        }
  		})
      // just for debug, remove if necessary
      .success(function() {console.log("Playlist Updated!")})
      .error(function() 
      { 
        console.log("Error, stopping refresh!");
        clearInterval(playlistRefresh);
      })
    }
  	var playlistRefresh = setInterval(getPlaylist, 5000);
  });
});