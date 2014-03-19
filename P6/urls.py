from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'P5.views.home', name='home'),
    # url(r'^P5/', include('P5.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^home', 'Pract6.views.home', name='home'),
    url(r'^help', 'Pract6.views.help', name='help'),
    url(r'^about','Pract6.views.about', name='about'),   
	
)
