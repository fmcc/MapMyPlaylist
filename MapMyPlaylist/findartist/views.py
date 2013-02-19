from findartist.models import Artist, Location
from findartist.utils.CreateArtist import CreateArtist
from django.shortcuts import render_to_response, get_object_or_404

def artistQuery(request, artistName):
    try:
        artist = Artist.objects.get(name=artistName)
    except Artist.DoesNotExist:
        CreateArtist(artistName)
        artist = Artist.objects.get(name=artistName)
    return render_to_response('findartist.html',{'artist': artist})
