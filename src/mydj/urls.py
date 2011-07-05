from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^community/$', 'community.views.index'),
    (r'^community/(?P<googlegroup_id>\d+)/$', 'community.views.detail'),
    # Examples:
    # url(r'^$', 'mydj.views.home', name='home'),
    # url(r'^mydj/', include('mydj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
