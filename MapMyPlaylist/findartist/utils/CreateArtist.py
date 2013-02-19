import pylast
import musicbrainzngs
from findartist.models import Artist, Location
from findartist.utils.DBPediaScanner import DBPediaScanner

class CreateArtist:
    API_KEY = 'b9403e2443856fa0ddbc7dd991c5f6c8'
    API_SECRET = '3030c906e7dfc4e12be5242fd0711604'
    username = 'MapMyPlaylist'
    password_hash = pylast.md5('playlistmymap')

    def __init__(self, BandName):
        newArtist = Artist()
        newLocation = Location()

        network = pylast.LastFMNetwork(api_key = self.API_KEY, api_secret = self.API_SECRET, username = self.username, password_hash = self.password_hash)
        LastFMartist = network.get_artist(BandName)
        
        newArtist.name = LastFMartist.get_name()
        newArtist.image = LastFMartist.get_cover_image()
        scanDBP = DBPediaScanner(newArtist.name)
        newArtist.bio = scanDBP.artistComment()
        locURI = scanDBP.artistLocationURI()
        if locURI != None:
            try:
                newArtist.origin = Location.objects.get(dbpediaURI = locURI)
                print 'Loc Found in DB'
            except Location.DoesNotExist:
                place = scanDBP.artistLocationLabel()
                latlong = scanDBP.artistLocationGeo()

                newArtist.origin = Location.objects.create(
                        placename = place,
                        latitude = latlong[0],
                        longitude = latlong[1],
                        dbpediaURI = locURI
                        )
                print 'Loc not Found in DB'
        else:
            unknown = Location.objects.get_or_create(
                    placename = 'Unknown',
                    latitude = 'Unknown',
                    longitude = 'Unknown',
                    dbpediaURI = 'Unknown'
                    )
            newArtist.origin = unknown[0]
            print 'Loc Unknown'

        newArtist.save()
        


