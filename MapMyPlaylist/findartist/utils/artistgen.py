from findartist.models import Artist, Location
from django.utils.simplejson import dumps, loads, JSONEncoder
from django.core import serializers
from findartist.utils.CreateArtist import CreateArtist

def packageArtists(artists):
    playlist = []
    for art in artists:
        a = artistGetOrCreate(art)
        playlist.append({'name': a.name,'bio': a.bio,'img_url': a.image,'origin': a.origin.placename,'lat': a.origin.latitude,'long': a.origin.longitude})
    return dumps(playlist)

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

