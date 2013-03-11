from findartist.models import Location
from findartist.utils.LocationLookup import LocationLookup
from findartist.utils.generic import MMPLFMACC

class CreateLocation:

	def __init__(self, locationName):
		newLocation = Location()
		scanDBP = LocationLookup(locationName)
		locURI = scanDBP.getLocationURI()
		locName = scanDBP.locationLabel()
		locGeo = scanDBP.locationGeo()

		if locURI != None:
			newLocation.dbpediaURI = locURI
			newLocation.placename = locName
			newLocation.latitude = locGeo[0]
			newLocation.longitude = locGeo[1]
			newLocation.save()
		else:
			print "Nuh!"
