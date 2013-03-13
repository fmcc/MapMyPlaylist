var tiles = "http://tile.stamen.com/toner/{z}/{x}/{y}.png";	 //default
var overlay = L.tileLayer(tiles);		//chosen tile for mapping
var layersControl = new L.Control.Layers({},{},{collapsed: true});

//creates the map
function createMap(){
	map = new L.Map('map', { minZoom: 3, maxBounds: ([[-90,180],[90, -180]])});
	map.addLayer(overlay);
        layersControl.addBaseLayer(overlay, "Tiles").addTo(map);
	return map;
}

//changes the map appearance based on user input
function changeTiles(form){
	for (Count = 0; Count < 4; Count++) {
        	if (form.display[Count].checked)
        	break;    	
	}
	layersControl.removeLayer(overlay);
	//if "toner"
    	if (Count == 0){
		tiles = "http://tile.stamen.com/toner/{z}/{x}/{y}.png";
	}
	//if "watercolour"
	if (Count == 1){
		tiles = "http://tile.stamen.com/watercolor/{z}/{x}/{y}.png";	
	}
	//if "greyscale"
    	if (Count == 2){
		tiles = "http://a.www.toolserver.org/tiles/bw-mapnik/{z}/{x}/{y}.png"; 
	}
	//if "openstreetmap"
	if (Count == 3){			
		tiles = "http://otile1.mqcdn.com/tiles/1.0.0/osm/{z}/{x}/{y}.png";
	}
	overlay = L.tileLayer(tiles);
	overlay.addTo(map);	
	layersControl.addBaseLayer(overlay, "Tiles");	
}

