(function() 
{
	function setMarker(lat, long, label)
	{
		console.log("Label should be " + label);
		var location = new L.LatLng(lat, long);
		var marker = new L.Marker(location, label);
		map.addLayer(marker);
	}
	//lat, lon and zoom of the map
    //TO DO: make it depend on the locations of the markers
	var lat            = 53.52;
	var lon            = -1.00;
	var zoom           = 2;
	
	//add map as baselayer	
	var map = new L.Map('map');
	var basemap  = new L.TileLayer("http://tile.stamen.com/toner/{z}/{x}/{y}.png");
	//map.setView(new L.LatLng(lat, lon), zoom);
	map.addLayer(basemap);

	function onLocationFound(e) 
	{
		var radius = e.accuracy / 2;

		L.marker(e.latlng).addTo(map)
		.bindPopup("You are within " + radius + "meters from this point").openPopup();

		L.circle(e.latlng, radius).addTo(map);
	}

	function onLocationError(e) {alert(e.message)}

	map.on('locationfound', onLocationFound);
	map.on('locationerror', onLocationError);

	map.locate({setView: true, maxZoom: 8});

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
		            		var latitude = parseFloat(this.lat);
		            		var longitude = parseFloat(this.long);
		            		if(isNaN(latitude))
		            		{
		                		console.log(this.name + " map failed!")
		                		return true;
		            		}
		            		var image = this.image;
		            		setMarker(latitude, longitude, this.name)
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


    
    var littleton = L.marker([39.61, -105.02]).bindPopup('This is Littleton, CO.');
    //    denver    = L.marker([39.74, -104.99]).bindPopup('This is Denver, CO.'),
    //    aurora    = L.marker([39.73, -104.8]).bindPopup('This is Aurora, CO.'),
    //    golden    = L.marker([39.77, -105.23]).bindPopup('This is Golden, CO.');
    //var cities = L.layerGroup([littleton, denver, aurora, golden]);
    //Display coordinates on the map
    map.addLayer(littleton);
    // map.addLayer(cities);
    
    
    
    
    
    
    
    
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
