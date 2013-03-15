from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'mapfrontend.views.mainpage'),
    url(r'^register/$', 'mapfrontend.views.register'),
    url(r'^ajaxlogin/$', 'mapfrontend.views.ajaxLogin'),
    url(r'^user/(?P<username>\w+)/$', 'mapfrontend.views.userpage'),

    url(r'^findartist/(?P<artistName>.+)/$', 'findartist.views.artistQuery'),
    url(r'^finduserplaylist/(?P<lastFMUsername>.+)/$', 'findartist.views.playlistQuery'),
    url(r'^findtopartists/(?P<lastFMUsername>.+)/$', 'findartist.views.topArtistQuery'),
    url(r'^allartists/$', 'findartist.views.findallartists'),
    url(r'^suggestartists/', 'findartist.views.suggestArtists', name='suggestartists'),
    url(r'^suggestlocations/', 'findartist.views.suggestLocations', name='suggestlocations'),
    url(r'^addorigin/(?P<locName>.+)/$', 'findartist.views.addOrigin'),
)
