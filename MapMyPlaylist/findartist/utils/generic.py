import pylast
def MMPLFMACC():
    API_KEY = 'b9403e2443856fa0ddbc7dd991c5f6c8'
    API_SECRET = '3030c906e7dfc4e12be5242fd0711604'
    username = 'MapMyPlaylist'
    password_hash = pylast.md5('playlistmymap')
    return pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)
