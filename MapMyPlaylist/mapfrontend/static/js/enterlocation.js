
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

$( document ).ready(function(){
	$("#MMP_unknown_artist_prompt").hide();
});


function addUnknownOrigin(artist) {
	var name = artist.name;
	$("#MMP_unknown_artist_prompt").toggle().html('');
	var textBox = $('<input>')
	.prop('type', 'text').val($(name).text())
	.prop('id', 'originbox');

	var button = $('<input>')
	.prop('type', 'submit').val($(name).text())
	.prop('id', 'originbutton')
	.width(40);

	$("#MMP_unknown_artist_prompt").append(name).append(textBox).append(button);
	setArtist(name);
}

function addOrigin(artist, location) {
	$.post('/addorigin/' + location + '/', artist, function() {
		$("#MMP_unknown_artist_prompt").html('').hide();
		console.log(artist + " is from " + location);
	});
}

function setArtist(name){
    $("#originbutton").click(function() {
    	var loc = $('#originbox').val();
		$.getJSON('/findartist/' + name + '/', function(data){
		addOrigin(data[0], loc)
		});			
	});
}

$(function() {
    $("#locationbox").autocomplete( {
        source: "/suggestlocations/",
        minLength: 1,
    }).autocomplete("option", "appendTo", "#locationentry");
});