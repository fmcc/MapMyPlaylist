from findartist.models import Artist, Location
from findartist.utils.CreateArtist import CreateArtist
from findartist.utils.LastFMPlaylist import LastFMPlaylist
from django.shortcuts import render_to_response, get_object_or_404
from django.http import  HttpResponse 
from django.utils.simplejson import dumps, loads, JSONEncoder
from django.core import serializers

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
    user = LastFMPlaylist(lastFMUsername)
    artists = user.getPlaylist()
    playlist = []
    for art in artists:
        a = artistGetOrCreate(art)
        playlist.append({'name': a.name,'bio': a.bio,'img_url': a.image,'origin': a.origin.placename,'lat': a.origin.latitude,'long': a.origin.longitude})
    json_playlist = dumps(playlist)
    return HttpResponse(json_playlist, content_type="application/json")

"""
Method to either retrieve an artist from the database, or use the CreateArtist Class to query last.fm and dbpedia and add the artist to our DB.
"""
def artistGetOrCreate(artistName):
    try:
        artist = Artist.objects.get(name=artistName)
    except Artist.DoesNotExist:
        CreateArtist(artistName)
        artist = Artist.objects.get(name=artistName)
    return artist

def suggestEntry(request):
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
