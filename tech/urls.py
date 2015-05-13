from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # TechSite:
    url(r'^$', 'techsite.views.home', name='home'),

    # Techblog :
    url(r'^techblog/$', 'techblog.views.home', name='techblog'),

    # Admin
    # url(r'^admin/', include(admin.site.urls)),
)
