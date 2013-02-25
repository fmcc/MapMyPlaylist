from findartist.models import Artist, Location
from findartist.utils.CreateArtist import CreateArtist
from findartist.utils.LastFMPlaylist import LastFMPlaylist
from django.shortcuts import render_to_response, get_object_or_404

def artistQuery(request, artistName):
    artist = artistGetOrCreate(artistName)
    return render_to_response('findartist.html',{'artist': artist})

def playlistQuery(request, lastFMUsername):
    user = LastFMPlaylist(lastFMUsername)
    artists = user.getPlaylist()
    playlist = []
    for art in artists:
        playlist.append(artistGetOrCreate(art))
    return render_to_response('playlist.html',{'playlist': playlist})

def artistGetOrCreate(artistName):
    try:
        artist = Artist.objects.get(name=artistName)
    except Artist.DoesNotExist:
        CreateArtist(artistName)
        artist = Artist.objects.get(name=artistName)
    return artist
