import DBPediaScanner

artist = raw_input('Enter the artist name:').strip()
dbPediaScanner = DBPediaScanner.DBPediaScanner(artist)
locURI = dbPediaScanner.artistLocationURI()
ht = dbPediaScanner.artistLocationLabel()
type(ht)
dbPediaScanner.artistLocationGeo()