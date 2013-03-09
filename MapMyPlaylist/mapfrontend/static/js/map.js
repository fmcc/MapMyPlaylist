(function() 
{
	function setMarker(lat, long, label, image, summary)
	{
		console.log("Label should be " + label);
		//custom marker		
		var musicIcon = L.icon(
		{
        	iconUrl:'static/img/pin_pink.png',
        	iconSize: [50,50],
		iconAnchor: [15,49]
    		});
   
    	var location = new L.LatLng(lat, long);
    	//this adds a html popup with an image and a summary 
  		var marker = L.marker(location, {title: label, icon: musicIcon}).bindPopup("<table><tr><td><img src=" + image + " height=100% width=100%></td><td>" + summary + "</td></tr></table>");
		map.addLayer(marker);
	}
	
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

	$( document ).ready(function() 
	{
		$('#searchbutton').click(function()
		{
    		var username = $('#searchbox').val();
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
		        		var userLat = userMarker.getLatLng().lat;
		        		var userLong = userMarker.getLatLng().lng;
		        		var minLatLng = [userLat, userLong];
		        		var maxLatLng = [userLat, userLong];
		        		$.each(data, function() 
		          		{ // displays artist names currently for display purposes
		            		var latitude = parseFloat(this.lat);
		            		var longitude = parseFloat(this.long);
		            		if(isNaN(latitude))
		            		{
		                		console.log(this.name + " map failed!")
		                		return true;
		            		}
		            		if(latitude < minLatLng[0]) { minLatLng[0] = latitude }
		            		if(latitude > maxLatLng[0]) { maxLatLng[0] = latitude }
		            		if(longitude < minLatLng[1]) { minLatLng[1] = longitude }
		            		if(longitude > maxLatLng[1]) { maxLatLng[1] = longitude }
					//sets a marker for this artist					
					setMarker(latitude, longitude, this.name, this.img_url, this.bio)
		          		});
		          		$('#artists').html(artists);
		          		latestArtist = data[0].name;
		          		if(userLong < minLatLng[1]) { minLatLng[1] = userLong }
		            	if(userLong > maxLatLng[1]) { maxLatLng[1] = userLong }
		            	//alert("userLong is " + userLong);
		          		map.fitBounds([
		          			minLatLng,
		          			maxLatLng
		          			]);
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
})();
