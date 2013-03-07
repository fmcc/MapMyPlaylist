(function() 
{
	function setMarker(lat, long, label, image, summary)
	{
		console.log("Label should be " + label);
		//custom marker		
		var musicIcon = L.icon(
		{
        	iconUrl:'static/img/musicicon.png',
        	iconSize: [40,40]
    	});
   
    	var location = new L.LatLng(lat, long);
    	//this adds a html popup with an image and a summary 
  		var marker = L.marker(location, {title: label, icon: musicIcon}).bindPopup("<table><tr><td><img src=" + image + " height=100% width=100%></td><td>" + summary + "</td></tr></table>");
		map.addLayer(marker);
	}
	
	//add map as baselayer	
	//var map = new L.Map('map', {minZoom: 2});
	//var basemap  = new L.TileLayer("http://tile.stamen.com/toner/{z}/{x}/{y}.png");
	//var basemap  = new L.TileLayer("http://tile.stamen.com/watercolor/{z}/{x}/{y}.png");
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
		var radius = e.accuracy / 2;

		userMarker = L.marker(e.latlng).addTo(map)
		.bindPopup("You are within " + radius + "meters from this point").openPopup();

		L.circle(e.latlng, radius).addTo(map);
	}

	function onLocationError(e) {alert(e.message)}

	map.on('locationfound', onLocationFound);
	map.on('locationerror', onLocationError);

	map.locate({setView: true, maxZoom: 7});

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
		            		//setMarker(latitude, longitude, this.name)
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
    
    //Raphael and Leaflet working together....
    //useless really...
	/*map.on('click', function(e) {
		var b = new R.BezierAnim([adelaide, e.latlng], {}, function() {
			var p = new R.Pulse(
					e.latlng, 
					6,
					{'stroke': '#ffff00', 'fill': '#30a3ec'}, 
					{'stroke': '#30a3ec', 'stroke-width': 3});

			map.addLayer(p);
			setTimeout(function() {
				map.removeLayer(b).removeLayer(p);
			}, 3000);
		});
		map.addLayer(b);
     
	});
    */
})();


/*var node = Raphael(0,0,500,500);
node.circle(150,150,5);

function arcs(cenx, ceny, radius, linewidth, pos) {
    openW = 300;
    openH = 100;
    bigR = radius + linewidth;
    arc = [
        ["M",cenx, ceny - radius],
        ["a",radius,radius,0,0,1,radius,radius],
        ["l",linewidth,0],
        ["a",bigR,bigR,0,0,0,-bigR,-bigR],
        ["l",0,linewidth]
        ];
    openedArc = [
        ["M",cenx, ceny - radius],
        ["a",radius,radius,0,0,1,radius,radius],
        ["l",openW,0],
        ["l",0,-openH],
        ["l",-openW-radius,0],
        ["l",0,openH-radius]
        ];
    node.path(arc).attr({"fill": "#f00"}).transform([["r",pos,150,150]])
    .click(function(){
        this.animate({path: openedArc}, 500, "<");
    }).dblclick(function(){
        this.animate({path: arc}, 500, "<");
    });;
}

arcs(150,150,20,20,0);
arcs(150,150,20,20,90);
arcs(150,150,20,20,180);
arcs(150,150,20,20,270);
*/
