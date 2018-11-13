from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from myproj.views import index



urlpatterns = [
#    url(r'^$', 'myproj.views.index', name='index'),

   url(r'^hello/', index),
 url(r'^webapp/', include('publik.urls')),
    # Examples:
    # url(r'^$', 'myproj.views.home', name='home'),
    # url(r'^myproj/', include('myproj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
