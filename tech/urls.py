from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # TechSite:
    url(r'^$', 'techsite.views.home', name='home'),

    # Convergence :
    url(r'^convergence/', 'convergence.views.home', name='convergence'),

    # Techblog : 
    url(r'^techblog/', 'techblog.views.home', name='techblog'),

    url(r'^admin/', include(admin.site.urls)),
)
