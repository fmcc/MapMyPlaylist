import pylast
import getpass
import re
import textwrap


API_KEY = 'b9403e2443856fa0ddbc7dd991c5f6c8'
API_SECRET = '3030c906e7dfc4e12be5242fd0711604'
username = raw_input("What's your username (for API authentication)?\n")
password_hash = pylast.md5(getpass.getpass("What's your password (for API authentication)?\n"))


network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)

artist = network.get_artist(raw_input("Username to Query?\n"))
nohtml = re.sub("<.*?>", "", artist.get_bio_content())

bio = textwrap.fill(nohtml, 80)
print(bio)




