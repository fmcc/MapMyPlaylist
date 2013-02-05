import rdflib
import re

OBJECT_INDEX = 1;
DBONTO = rdflib.Namespace('http://dbpedia.org/ontology/')
ONTOLOGIES = (DBONTO.hometown, DBONTO.birthPlace)

def artistLocationInfo(artist, ontology):
	artistURI = "http://dbpedia.org/resource/" + re.sub('\s+', '_', artist)
	artistGraph = rdflib.Graph()
	artistGraph.parse(artistURI)
	artistGraph = checkDisambiguates(artistURI, artistGraph)
	lat = list()
	lon = list()
	locationGraph = rdflib.Graph()

	# TODO: Sort out hometown vs birthPlace vs origin etc also property vs ontology
	for statement in artistGraph.subject_objects(ontology):
		locationGraph.parse(statement[OBJECT_INDEX])
		hometown = locationGraph.preferredLabel(statement[OBJECT_INDEX], lang=u'en')[0][1]
		if len(hometown) > 0:
			break

	if len(locationGraph) is 0:
		return False

	for statement in locationGraph.subject_objects(rdflib.URIRef("http://www.w3.org/2003/01/geo/wgs84_pos#lat")):
		lat.append(float(statement[OBJECT_INDEX]))
	for statement in locationGraph.subject_objects(rdflib.URIRef("http://www.w3.org/2003/01/geo/wgs84_pos#long")):
		lon.append(float(statement[OBJECT_INDEX]))

	if len(lat) > 1:
		latitude = (lat[0] + lat[1]) / 2
	elif len(lat) == 0:
		print "No geodata!"
		return False
	else:
		latitude = lat[0]

	if len(lon) > 1:
		longitude = (lon[0] + lon[1]) / 2 # Round this?
	elif len(lon) == 0:
		print "No geodata!"
		return False
	else:
		longitude = lon[0]	

	locationInfo = {'town': str(hometown), 'latitude': latitude, 'longitude': longitude}

	print "Hometown is ", locationInfo['town']
	print "Latitude is ", locationInfo['latitude']
	print "Longitude is ", locationInfo['longitude']

	return True

def checkDisambiguates(artistURI, graph):
	newGraph = rdflib.Graph()
	for stmt in graph.objects(rdflib.URIRef(artistURI), DBONTO.wikiPageDisambiguates):
		disamb = str(stmt)
		if '(band)' in disamb:
			newGraph.parse(stmt)
			print "Disambiguated to :", disamb
			break
		elif '(singer)' in disamb:
			newGraph.parse(stmt)
			print "Disambiguated to :", disamb
			break
		elif '(group)' in disamb:
			newGraph.parse(stmt)
			print "Disambiguated to :", disamb
			break
		elif '(musician)' in disamb:
			newGraph.parse(stmt)
			print "Disambiguated to :", disamb
			break

	if len(newGraph) > 0:
		return newGraph
	else:
		return graph

artist = raw_input('Enter the artist name:').strip()

for ontology in ONTOLOGIES:
	if artistLocationInfo(artist, ontology):
		break

print "Finished!"





