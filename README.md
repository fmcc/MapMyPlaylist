===============
Map My Playlist
===============


Dependencies
------------
The following python libraries/packages are used by Map My Playlist, and will require installation. 

* pylast
* rdflib
* guess-language

Github:
-------

The git repository for this project can be found at:

``https://github.com/GraemeEArthur/MapMyPlaylist/``

Running Map My Playlist
-----------------------

Map My Playlist can be run locally with the following command:

`` python ./manage.py runserver ``

The home page can then be accessed at the following url: 

``http://127.0.0.1:8000/``

An example of a user profile page can be viewed at:

``http://127.0.0.1:8000/user/finlay``


DB repopulation
---------------

Should there be an issue with the database, it can be re-populated by running the following command:

`` python ./manage.py loaddata ./MMP_DB_backup.json ``
