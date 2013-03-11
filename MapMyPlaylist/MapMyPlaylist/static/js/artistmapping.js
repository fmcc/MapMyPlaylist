function testButton (form){
	for (Count = 0; Count < 2; Count++) {
        	if (form.display[Count].checked)
        	break;
    	}
	//if "map recently listened"
    	if (Count == 0){
		alert ("Map recently listened is selected");
		//TODO
		//needs data
		//needs map
		//needs minLatLng
		//needs maxLatLng
		
	}
	//if "map top artists"
	if (Count == 1){
		alert ("Map top arists is selected");		
		//TODO
		//needs data
		//needs map
		//needs minLatLng
		//needs maxLatLng
	}
}

function createMap(){
    var toner = new L.TileLayer("http://tile.stamen.com/toner/{z}/{x}/{y}.png");
    var map = new L.Map('map', { minZoom: 2, layers: [toner]});
    var baseLayers = {"Toner": toner};
    L.control.layers(baseLayers).addTo(map);
    return map;
}

function plotArtists(artists, map, minLatLng, maxLatLng){
    $.each(artists, function(){ 
        var latitude = parseFloat(this.lat);
	var longitude = parseFloat(this.long);
        if(isNaN(latitude)){
	    alert ("Map My Playlist doesn't know where " + this.name + " is from");
            console.log(this.name + " map failed!");
	    return true;
        }
	if(latitude < minLatLng[0]) { minLatLng[0] = latitude };
	if(latitude > maxLatLng[0]) { maxLatLng[0] = latitude };
	if(longitude < minLatLng[1]) { minLatLng[1] = longitude };
	if(longitude > maxLatLng[1]) { maxLatLng[1] = longitude };
        artist={lat:latitude,long:longitude,label:this.name,image:this.img_url,summary:this.bio};
        setMarker(artist, map);
        })
};

function setMarker(artist, map){
    //#FFAE4A
    //#3FD98B
    //#EF4581
    var location = new L.LatLng(artist.lat, artist.long);
    var test = new L.CircleMarker(location, {color: 'black', opacity: '1', fillColor:'#FFAE4A', fillOpacity:'0.8'}).bindPopup(artist.label);
    map.addLayer(test);
};

