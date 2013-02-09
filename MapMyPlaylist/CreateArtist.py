import pylast
from findartist.models import Artist, Location

class CreateArtist(self, BandName):
    API_KEY = 'b9403e2443856fa0ddbc7dd991c5f6c8'
    API_SECRET = '3030c906e7dfc4e12be5242fd0711604'
    username = 'wildfreenoise'
    password_hash = pylast.md5('hipflask121')
    network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)

    newArtist = Artist()
    newLocation = Location()

    LastFMartist = network.get_artist(BandName)
    
    newArtist.name = LastFMartist.get_name()
    newArtist.image = LastFMartist.get_cover_image()
    newArtist.bio = LastFMartist.get_bio_summary() 



