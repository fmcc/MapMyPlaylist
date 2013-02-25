from findartist.models import Artist, Location
from findartist.utils.CreateArtist import CreateArtist
from findartist.utils.LastFMPlaylist import LastFMPlaylist
from django.shortcuts import render_to_response, get_object_or_404
from django.http import  HttpResponse 
from django.utils.simplejson import dumps, loads, JSONEncoder
from django.core import serializers

def artistQuery(request, artistName):
    a = artistGetOrCreate(artistName)
    artist = []
    artist.append({'name': a.name,'bio': a.bio,'img_url': a.image,'origin': a.origin.placename,'lat': a.origin.latitude,'long': a.origin.longitude})
    json_artist = dumps(artist)
    return HttpResponse(json_artist, content_type="application/json")

def playlistQuery(request, lastFMUsername):
    user = LastFMPlaylist(lastFMUsername)
    artists = user.getPlaylist()
    playlist = []
    for art in artists:
        a = artistGetOrCreate(art)
        playlist.append({'name': a.name,'bio': a.bio,'img_url': a.image,'origin': a.origin.placename,'lat': a.origin.latitude,'long': a.origin.longitude})
    json_playlist = dumps(playlist)
    return HttpResponse(json_playlist, content_type="application/json") 

def artistGetOrCreate(artistName):
    try:
        artist = Artist.objects.get(name=artistName)
    except Artist.DoesNotExist:
        CreateArtist(artistName)
        artist = Artist.objects.get(name=artistName)
    return artist
