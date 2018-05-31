from __future__ import absolute_import, unicode_literals

from django.urls import path

from django.conf.urls import include, url

from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('sampleapp/', include('sampleapp.urls')),
    #path('', tasks.index, name='index'),
    url(r'^admin/', admin.site.urls),
]






