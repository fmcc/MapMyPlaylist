    //global variables
    var map = "";			//map variable
    var userMarker = {};		//marker for the user
    var currentLFMUserName = "" ;
    var minLatLng = [];		//minimum latitude and longitude
    var maxLatLng = [];		//maximum latitude and longitude
    var mappingSuccessful = "";	//set to successful if number of markers added is greater than 0
    var latestArtist = "";		//variable to keep track of the latest artist
    var hold = false;		//hold is true if mapping shouldn't be refreshed
    var tiles = "http://tile.stamen.com/toner/{z}/{x}/{y}.png";		//chosen tile for mapping
    var baseLayers= "";		//base layer to add to map
    var markerColours = ["#FFAE4A", "#3FD98B", "#EF4581", "#6AA6E2", "#A66AE2", "#E26A6A", "#D52A2A", "#D5D52A", "#90E9BD", "#2AD5D5", "#D52AD5", "#EDA6C9", "#6AE26A"];

//initialises the page
function init(){
	var map = createMap();
	//plots a marker of the user's location
        function onLocationFound(e){
                userMarker = new L.CircleMarker(e.latlng, {radius: '20',color: 'black', opacity: '1', fillColor:'#A66AE2', fillOpacity:'0.8'}).addTo(map);
        }
        function onLocationError(e) {alert(e.message)}
        map.on('locationfound', onLocationFound);
        map.on('locationerror', onLocationError);
        map.locate({setView: true, maxZoom: 7});                 
}
//creates the map
function createMap(){
	//adds the tilelayer toner from Stamen to the map	
	var toner = new L.TileLayer(tiles);
	map = new L.Map('map', { minZoom: 3, maxBounds: ([[-90,180],[90, -180]]), layers: [toner]});
   	baseLayers = {"Toner": toner};
	L.control.layers(baseLayers).addTo(map);
	return map;
}

//gets the artist data where name is either bandname or playlistname 
function getData(user_details, query_type){
    var playlistRefresh;
    if(query_type == "MMP_recent"){
        console.log(user_details.lfmusername); 
        console.log(currentLFMUserName); 
        if(user_details.lfmusername != currentLFMUserName){
            console.log("aye");
            var friendLoc = new L.LatLng(parseFloat(user_details.latitude) , parseFloat(user_details.longitude));
            var friendMarker = new L.CircleMarker(friendLoc, {radius: '20',color: 'black', opacity: '1', fillColor:'#A66AE2', fillOpacity:'0.8'}).addTo(map);
        } 
        $.getJSON('/finduserplaylist/' + user_details.lfmusername + '/', function(data){
	    setMinMaxLatLng();
	    // checks to see if most recent artist has changed
    	    if (data[0].name != latestArtist){			
                plotArtists(data, map);
		}
	    //refreshes the getData function if it is not on hold
	    playlistRefresh = setInterval(function(){
	        if(hold) {
		    return;
		}
		getData("playlist",name)}, 2000); 
        	})
	}
    
    if(query_type == "MMP_top"){
        $.getJSON('/findtopartists/' + user_details.lfmusername + '/', function(data){
	    setMinMaxLatLng();
            plotArtists(data, map);
        })
    }
}

//sets the minimum and maximum latitude and longitude 
//to the user's location 
function setMinMaxLatLng(){
	var userLat = userMarker.getLatLng().lat;
        var userLong = userMarker.getLatLng().lng;
        minLatLng = [userLat, userLong];
        maxLatLng = [userLat, userLong];
}

//plots the artist on the map
function plotArtists(artists, query_type){
    colour = markerColours[Math.floor(Math.random()*markerColours.length)];
    var mappedArtists = []
    mappingSuccessful = false;
    $.each(artists, function(){ 
        var latitude = parseFloat(this.lat);
	var longitude = parseFloat(this.long);
        if(isNaN(latitude)){
	    enterLocation(this);
	    hold = true;
	    return true;
        }
	else{
	    	if(latitude < minLatLng[0]) { minLatLng[0] = latitude };
	    	if(latitude > maxLatLng[0]) { maxLatLng[0] = latitude };
	    	if(longitude < minLatLng[1]) { minLatLng[1] = longitude };
	    	if(longitude > maxLatLng[1]) { maxLatLng[1] = longitude };
            	artist={lat:latitude,long:longitude,label:this.name,image:this.img_url,summary:this.bio};
            	mappedArtists.push(setMarker(artist, colour));
	}
    })
    hold = false;
    latestArtist = artists[0].name;
    //if at least one marker has been added, adjust the bounds of the map
    if(mappingSuccessful){
        map.fitBounds([minLatLng,maxLatLng]);
    }   
    return mappedArtists ; 
};

//sets a marker for a location of an artist
function setMarker(artist, colour){
    var location = new L.LatLng(artist.lat, artist.long);
    var marker = new L.CircleMarker(location, {color: 'black', opacity: '1', fillColor: colour, fillOpacity:'0.8'}).bindPopup(
            '<img id="artist-popup-image" src="' + 
            artist.image + 
            '" align="right">' + 
            '<div id="artist-popup-title">' +
            artist.label + 
            '</div>' +
            '<div id="artist-popup-bio">' +
            artist.summary +
            '</div>'
            );
    map.addLayer(marker);
    var polyline = L.polyline([location , userMarker.getLatLng()], {color: colour}).addTo(map)
    mappingSuccessful = true;
    return marker ;
};

function MMP_update_plotting(){
    $(".MMP_plotting_checkbox").each(function(){
        if($(this).is(':checked')){
            var user_details ={
                lfmusername: $(this).data('user_lfm'),
                latitude: $(this).data('user_lat'),
                longitude: $(this).data('user_lng')
                };
         getData(user_details, $(this).attr("id"));
        }
    });
}

$( document ).ready(function(){
    currentLFMUserName = $("#MMP_current_user").text();
    $("#MMP_search_clear_button").hide(); 
    init();
    var artistSearchResults = [] ; 
    MMP_update_plotting();
    // Used to search for individual 
    $('#MMP_search_button').click(function(){
        var artist_name = $('#MMP_search_box').val();
        var query_type = "MMP_search";
        $.getJSON('/findartist/' + artist_name + '/', function(data){
        setMinMaxLatLng();      
        artistSearchResults = artistSearchResults.concat(plotArtists(data, query_type));
        })
    });
    var needCleared = setInterval( function(){
        if(artistSearchResults.length >= 1){
            $("#MMP_search_clear_button").show(); 
        }else{
            $("#MMP_search_clear_button").hide(); 
        }
    },500);

    $('#MMP_search_clear_button').click(function(){
        $.each(artistSearchResults, function() {
            map.removeLayer(artistSearchResults.pop(this));
    });
    });

    $("#MMP_search_box").autocomplete({ source: "/suggestartists/", minLength: 1, });
});


