from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MapMyPlaylist.views.home', name='home'),
    # url(r'^MapMyPlaylist/', include('MapMyPlaylist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', 'mapfrontend.views.mainpage'),
    url(r'^register/$', 'mapfrontend.views.register'),
    url(r'^user/(?P<username>\w+)/$', 'mapfrontend.views.userpage'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^findartist/(?P<artistName>.+)/$', 'findartist.views.artistQuery'),
    url(r'^finduserplaylist/(?P<lastFMUsername>.+)/$', 'findartist.views.playlistQuery'),
    url(r'^findtopartists/(?P<lastFMUsername>.+)/$', 'findartist.views.topArtistQuery'),
    url(r'^allartists/$', 'findartist.views.findallartists'),
    url(r'^suggestartists/', 'findartist.views.suggestArtists', name='suggestartists'),
    url(r'^suggestlocations/', 'findartist.views.suggestLocations', name='suggestlocations'),
    url(r'^findlocation/(?P<locName>.+)/$', 'findartist.views.locationQuery'),
)
