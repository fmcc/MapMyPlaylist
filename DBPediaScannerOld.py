import rdflib
import re

class DBPediaScanner:
	DBONTO = rdflib.Namespace('http://dbpedia.org/ontology/')
	ONTOLOGIES = (DBONTO.hometown, DBONTO.birthPlace)

	labelPredicate = rdflib.term.URIRef(u'http://www.w3.org/2000/01/rdf-schema#label')
	latPredicate = rdflib.URIRef("http://www.w3.org/2003/01/geo/wgs84_pos#lat")
	longPredicate = rdflib.URIRef("http://www.w3.org/2003/01/geo/wgs84_pos#long")
	locationGraph = rdflib.Graph()

	def __init__(self, artist):
		self.artistURI = "http://dbpedia.org/resource/" + re.sub('\s+', '_', artist)
		self.artistGraph = rdflib.Graph()
		self.artistGraph.parse(self.artistURI)
		self.__checkDisambiguates()

	def artistLocationURI(self, artist):
		for ontology in self.ONTOLOGIES:
			try:
				self.locationURI = self.artistGraph.subject_objects(ontology).next()
				print "Ontology of type", ontology, "found!"
				return self.locationURI
			except (IndexError, StopIteration):
				print "No ontology of type", ontology, "found!"

	def artistLocationLabel(self):
		self.locationGraph.parse(self.locationURI)
		try:
			hometown = str(self.locationGraph.preferredLabel(self.locationURI, lang=u'en')[0][1])
			print "English label found!"
			print "Hometown is", hometown
			return str(hometown)
		except IndexError:
			print "No English label found!"
			try:
				hometown = self.locationGraph.objects(self.locationURI, self.labelPredicate).next()
			except StopIteration:
				print "Empty locationGraph!" 

	def artistLocationGeo(self):
		try:
			lat = float(self.locationGraph.objects(self.locationURI, self.latPredicate).next())
			lon = float(self.locationGraph.objects(self.locationURI, self.longPredicate).next())
			print "Latitude is", lat
			print "Longitude is", lon
			return lat, lon
		except StopIteration:
			print "No geodata!"

	def __checkDisambiguates(self):
		for stmt in self.artistGraph.objects(rdflib.URIRef(self.artistURI), self.DBONTO.wikiPageDisambiguates):
			disamb = str(stmt)
			print "Disamb is:", disamb
			if '(band)' in disamb:
				self.__updateGraph(disamb)
				print "Disambiguated to :", disamb
			elif '(singer)' in disamb:
				self.__updateGraph(disamb)
				print "Disambiguated to :", disamb
			elif '(group)' in disamb:
				self.__updateGraph(disamb)
				print "Disambiguated to :", disamb
			elif '(musician)' in disamb:
				self.__updateGraph(disamb)
				print "Disambiguated to :", disamb

	def __updateGraph(self, newURI):
		self.artistURI = newURI
		self.artistGraph.parse(newURI)