import pylast
from findartist.utils.CreateArtist import CreateArtist
from findartist.utils.generic import MMPLFMACC

class LastFMPlaylist:

    def __init__(self, lastFMUsername):
        network = MMPLFMACC()
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


