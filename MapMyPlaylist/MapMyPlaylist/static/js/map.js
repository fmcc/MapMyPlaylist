(function() 
{
	//add map as baselayer	
	//var map = new L.Map('map', {minZoom: 2});
	//var basemap  = new L.TileLayer("http://tile.stamen.com/toner/{z}/{x}/{y}.png");
	//map.addLayer(basemap);

	var watercolour = new L.TileLayer("http://tile.stamen.com/watercolor/{z}/{x}/{y}.png");
	var osm =  new L.TileLayer("http://a.tile.openstreetmap.org/{z}/{x}/{y}.png");
	var mapQuest = new L.TileLayer("http://otile{s}.mqcdn.com/tiles/1.0.0/osm/{z}/{x}/{y}.png", {subdomains: ['1','2','3','4']});				
	var toner = new L.TileLayer("http://tile.stamen.com/toner/{z}/{x}/{y}.png");
	
	var map = new L.Map('map', {
		minZoom: 2,
		layers: [watercolour, osm, mapQuest, toner]	
	});

	var baseLayers = {
		"Watercolour": watercolour,
		"OSM": osm,
		"MapQuest": mapQuest,
		"Toner": toner
	};

	L.control.layers(baseLayers).addTo(map);

	var userMarker = {};
	function onLocationFound(e) 
	{
		//custom user marker		
		var userIcon = L.icon(
		{
        	iconUrl:'static/img/pin_green.png',
        	iconSize: [50,50],
		iconAnchor: [15,49]
		});		
						
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
