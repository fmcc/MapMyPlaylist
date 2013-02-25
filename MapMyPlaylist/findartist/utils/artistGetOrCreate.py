from findartist.models import Artist, Location
from findartist.utils.CreateArtist import CreateArtist

def artistGetOrCreate(artistName)
    try:
        artist = Artist.objects.get(name=artistName)
    except Artist.DoesNotExist:
        CreateArtist(artistName)
        artist = Artist.objects.get(name=artistName)
    return artist
