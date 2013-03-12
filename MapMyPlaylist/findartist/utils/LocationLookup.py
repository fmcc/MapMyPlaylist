import rdflib
import re
from urllib import quote_plus

class LocationLookup:

    DBONTO = rdflib.Namespace('http://dbpedia.org/ontology/') # Ontology rdflib Namespace

    latPredicate = rdflib.URIRef("http://www.w3.org/2003/01/geo/wgs84_pos#lat")
    longPredicate = rdflib.URIRef("http://www.w3.org/2003/01/geo/wgs84_pos#long")
    labelPredicate = rdflib.term.URIRef(u'http://www.w3.org/2000/01/rdf-schema#label')


    def __init__(self, locationName):
        self.locName = locationName.encode('utf-8')
        self.locURI = rdflib.URIRef(quote_plus('http://dbpedia.org/resource/' + re.sub('\s+', '_', locationName), safe='/:'))
        self.locGraph = rdflib.Graph().parse(self.locURI)

    def locationURI(self):
        return quote_plus(self.locURI, safe='/:')

    def locationLabel(self):
        try:
            locationLabel = self.locGraph.preferredLabel(self.locURI, lang=u'en')[0][1]
            print "English label found!"
            return locationLabel
        except IndexError: # If no labels in English are found
            print "No English label found!"
            try:
                hometown = self.locGraph.objects(self.locURI, self.labelPredicate).next()
                return hometown
            except StopIteration: # If generator is empty
                print "Empty locationGraph!"

    def locationGeo(self):
        try:
            lat = float(self.locGraph.objects(self.locURI, self.latPredicate).next())
            lon = float(self.locGraph.objects(self.locURI, self.longPredicate).next())
            print "Latitude is", lat
            print "Longitude is", lon
            return lat, lon
        except StopIteration: # If generator is empty
            print "No geodata!"
        except AttributeError: # If locationURI hasn't been defined
            print "LocationURI not defined!"
