
(function($){
    $.fn.plotArtists = function(){
        $.each(this, function(){ 
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
        })
    };
})(jQuery);

