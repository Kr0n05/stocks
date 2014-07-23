from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
		url(r'^admin/', include(admin.site.urls)),
		url(r'^get_news/$', 'sourcefeed_parser.views.get_news', name='sourcefeed_parser.views.get_news'),
)
