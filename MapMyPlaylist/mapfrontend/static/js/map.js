(function(){
    var map = createMap();
    var userMarker = {};
    function onLocationFound(e){
        var userIcon = L.icon({iconUrl:'static/img/pin_green.png',iconSize: [50,50],iconAnchor: [15,49]});
        var radius = e.accuracy / 2;
        userMarker = L.marker(e.latlng, {icon: userIcon}).addTo(map)    
        L.circle(e.latlng, radius).addTo(map);
    }
    function onLocationError(e) {alert(e.message)}
    map.on('locationfound', onLocationFound);
    map.on('locationerror', onLocationError);
    map.locate({setView: true, maxZoom: 7});


    $( document ).ready(function(){
        $('#searchbutton').click(function(){
            var bandname = $('#searchbox').val();
            function getPlaylist(){
                $.getJSON('/findartist/' + bandname + '/', function(data){
                    var userLat = userMarker.getLatLng().lat;
                    var userLong = userMarker.getLatLng().lng;
                    var minLatLng = [userLat, userLong];
                    var maxLatLng = [userLat, userLong];
                    plotArtists(data, map, minLatLng, maxLatLng)});
            }
        var playlistRefresh = setInterval(getPlaylist, 5000);
	})
  	});
})();
