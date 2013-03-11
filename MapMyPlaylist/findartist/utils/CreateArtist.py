import pylast
from findartist.models import Artist, Location
from findartist.utils.DBPediaScanner import DBPediaScanner
from findartist.utils.generic import MMPLFMACC

class CreateArtist:

    def __init__(self, BandName):
        newArtist = Artist()
        newLocation = Location()

        network = MMPLFMACC()
        LastFMartist = network.get_artist(BandName)
        
        newArtist.name = LastFMartist.get_name()
        newArtist.image = LastFMartist.get_cover_image()
        newArtist.musicbrainz = LastFMartist.get_mbid()
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
        


