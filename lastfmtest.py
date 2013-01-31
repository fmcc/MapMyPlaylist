import rdflib
from rdflib import Graph, URIRef

API_KEY = 'b9403e2443856fa0ddbc7dd991c5f6c8'
API_SECRET = '3030c906e7dfc4e12be5242fd0711604'
username = "wildfreenoise"
password_hash = pylast.md5("your_password")



band_name = raw_input("What's the band?\n")

g = rdflib.Graph()
band_URI = "http://dbpedia.org/resource/" + band_name

band = g.parse(band_URI)
for s in g.subject_objects(URIRef("http://dbpedia.org/ontology/hometown")):
        loc_g = rdflib.Graph()
        location = loc_g.parse(s[1])
        for t in loc_g.subject_objects(URIRef("http://www.w3.org/2003/01/geo/wgs84_pos#lat")):
            print(t[1])
        for t in loc_g.subject_objects(URIRef("http://www.w3.org/2003/01/geo/wgs84_pos#long")):
            print(t[1])
       # for t in loc_g.subject_objects(URIRef("http://www.w3.org/2000/01/rdf-schema#label")):
        #    print(t[1])




