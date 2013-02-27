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
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^findartist/(?P<artistName>.+)/$', 'findartist.views.artistQuery'),
    url(r'^finduserplaylist/(?P<lastFMUsername>.+)/$', 'findartist.views.playlistQuery'),
)
