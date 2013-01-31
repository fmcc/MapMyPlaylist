import rdflib
import re
import pylast
from rdflib import Graph, URIRef

API_KEY = 'b9403e2443856fa0ddbc7dd991c5f6c8'
API_SECRET = '3030c906e7dfc4e12be5242fd0711604'
username = raw_input("What's your username (for API authentication)?\n")
password_hash = pylast.md5(raw_input("What's your password (for API authentication)?\n"))


network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)

user = network.get_user(raw_input("Username to Query?\n"))

tracks = user.get_recent_tracks()

most_recent = tracks[0][0]
rec_art = most_recent.get_artist()

print(rec_art)




g = rdflib.Graph()
band_URI = "http://dbpedia.org/resource/" + rec_art.get_name()

band = g.parse(band_URI)
for s in g.subject_objects(URIRef("http://dbpedia.org/ontology/hometown")):
        loc_g = rdflib.Graph()
        location = loc_g.parse(s[1])
        for t in loc_g.subject_objects(URIRef("http://www.w3.org/2003/01/geo/wgs84_pos#lat")):
            print(t[1])
        for t in loc_g.subject_objects(URIRef("http://www.w3.org/2003/01/geo/wgs84_pos#long")):
            print(t[1])
        for t in loc_g.subject_objects(URIRef("http://www.w3.org/2000/01/rdf-schema#label")):
            print(t[1])




