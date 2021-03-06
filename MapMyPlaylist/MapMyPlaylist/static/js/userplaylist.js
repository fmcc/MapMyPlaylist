function createMap(){
    var toner = new L.TileLayer("http://tile.stamen.com/toner/{z}/{x}/{y}.png");
    var map = new L.Map('map', { minZoom: 2, layers: [toner]});
    var baseLayers = {"Toner": toner};
    L.control.layers(baseLayers).addTo(map);
    return map;
}

function addUser(map){
    var lat ;
    var lon ;
    function onLocationFound(e){
        var userIcon = L.icon({iconUrl:'static/img/pin_green.png',iconSize: [50,50],iconAnchor: [15,49]});		
	var radius = e.accuracy / 2;
	var userMarker = L.marker(e.latlng, {icon: userIcon}).addTo(map)
        lat = userMarker.getLatLng().lat;
        lon = userMarker.getLatLng().lng;
	L.circle(e.latlng, radius).addTo(map);
    }
    function onLocationError(e) {alert(e.message)}
    map.on('locationfound', onLocationFound);
    map.on('locationerror', onLocationError);
    map.locate({setView: true, maxZoom: 7});
    
    return [lat, lon]
}

function plotArtists(artists, map, minLatLng, maxLatLng){
    $.each(artists, function(){ 
        var latitude = parseFloat(this.lat);
	var longitude = parseFloat(this.long);
        if(isNaN(latitude)){
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
    map.fitBounds([minLatLng,maxLatLng]);
};

function setMarker(artist, map){
    var musicIcon = L.icon({iconUrl:'static/img/pin_pink.png',iconSize: [50,50],iconAnchor: [15,49]});
    var location = new L.LatLng(artist.lat, artist.long);
    var marker = L.marker(location, {title: artist.label, icon: musicIcon}).bindPopup("<table><tr><td><img src=" + artist.image + " height=100% width=100%></td><td>" + artist.summary + "</td></tr></table>");
    map.addLayer(marker);
};

