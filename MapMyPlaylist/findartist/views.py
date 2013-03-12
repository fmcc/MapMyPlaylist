from findartist.models import Artist, Location
from findartist.utils.LastFMInterface import LastFMInterface
from findartist.utils.artistgen import *
from findartist.utils.CreateLocation import CreateLocation
from django.shortcuts import render_to_response, get_object_or_404
from django.http import  HttpResponse 


"""
Takes an artist name from a url and returns that artist as a json object .
"""
def artistQuery(request, artistName):
    a = artistGetOrCreate(artistName)
    artist = []
    artist.append({'name': a.name,'bio': a.bio,'img_url': a.image,'origin': a.origin.placename,'lat': a.origin.latitude,'long': a.origin.longitude})
    json_artist = dumps(artist)
    return HttpResponse(json_artist, content_type="application/json")

"""
Takes in a username from a url and returns a list of unique artists from the last 10 (11?) artists listened to by that user on last.fm.
The information on each artist is converted to a dictionary object and appended to a list. This list is then converted to a json format via the 
simplejason.dumps method and this is returned via http. 
"""
def playlistQuery(request, lastFMUsername):
    user = LastFMInterface(lastFMUsername)
    artists = user.getPlaylist()
    return HttpResponse(packageArtists(artists), content_type="application/json")

def topArtistQuery(request, lastFMUsername):
    user = LastFMInterface(lastFMUsername)
    artists = user.getTopArtists()
    return HttpResponse(packageArtists(artists), content_type="application/json")

def findallartists(request):
    return HttpResponse(allArtists(), content_type="application/json")

def suggestArtists(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        artists = Artist.objects.filter(name__startswith=q).order_by("name")
        results = []
        for art in artists:
            artist_json = {}
            artist_json['id'] = art.name
            artist_json['label'] = art.name
            artist_json['value'] = art.name
            results.append(artist_json)
        data = dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def suggestLocations(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        locations = Location.objects.filter(placename__startswith=q).order_by("placename")
        results = []
        for loc in locations:
            location_json = {}
            location_json['id'] = loc.placename
            location_json['label'] = loc.placename
            location_json['value'] = loc.placename
            results.append(location_json)
        data = dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def locationQuery(request, locName):
    try:
        loc = Location.objects.get(placename=locName)
    except Location.DoesNotExist:
        try:
            CreateLocation(locName)
            loc = Location.objects.get(placename=locName)
        except Location.DoesNotExist:
            return HttpResponse("Location not found!")
    location = []
    location.append({'uri': loc.dbpediaURI, 'name': loc.placename, 'lat': loc.latitude, 'long': loc.longitude})
    json_location = dumps(location)
    return HttpResponse(json_location, content_type="application/json")