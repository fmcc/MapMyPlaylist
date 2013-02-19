from findartist.models import Artist, Location

def artistQuery(request, artistName):
    try:
        artist = Artist.objects.get(name=artistName)
    except Artist.DoesNotExist:
        artist = 

    try 
