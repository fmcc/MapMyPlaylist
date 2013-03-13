
function enterLocation(artist) { 
	$( "#locationentry" ).dialog( { 
		autoOpen: false, 
		title: "Enter Location for " + artist.name, 
		width: 350,
		height: 350, 
		modal: true 
	})
	.dialog("open");
	$('#locationbutton').click(function(){
		var location = $('#locationbox').val();
		addOrigin(artist, location);
		$( "#locationentry").dialog("close");
	});
};

function addOrigin(artist, location) {
	$.post('/addorigin/' + location + '/', artist
	)
};

$(function() {
    $("#locationbox").autocomplete( {
        source: "/suggestlocations/",
        minLength: 1,
    }).autocomplete("option", "appendTo", "#locationentry");
});