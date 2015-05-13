from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # TechSite:
    url(r'^$', 'techsite.views.home', name='home'),

    # Admin
    # url(r'^admin/', include(admin.site.urls)),
)
