from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # TechSite:
    url(r'^$', 'techsite.views.home', name='home'),

    # Convergence :
    url(r'^convergence/home', 'convergence.views.home', name='convergence'),
    url(r'^convergence/post', 'convergence.views.post', name='post'),

    # Techblog : 
    url(r'^techblog/', 'techblog.views.home', name='techblog'),

    url(r'^admin/', include(admin.site.urls)),
)
