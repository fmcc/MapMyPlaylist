import pylast
from findartist.utils.CreateArtist import CreateArtist

class LastFMPlaylist:
    API_KEY = 'b9403e2443856fa0ddbc7dd991c5f6c8'
    API_SECRET = '3030c906e7dfc4e12be5242fd0711604'
    username = 'MapMyPlaylist'
    password_hash = pylast.md5('playlistmymap')

    def __init__(self, lastFMUsername):
        network = pylast.LastFMNetwork(api_key = self.API_KEY, api_secret = self.API_SECRET, username = self.username, password_hash = self.password_hash)
        self.LastFMUser = network.get_user(lastFMUsername)

    def getPlaylist(self):
        artists = []
        if self.LastFMUser.get_now_playing() is not None:
            artists.append(self.LastFMUser.get_now_playing().get_artist().get_name())
        playlist = self.LastFMUser.get_recent_tracks()
        for p in playlist:
            art = p[0].get_artist().get_name()
            if art not in artists:
                artists.append(art)
        return artists


