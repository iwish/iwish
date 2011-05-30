from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       # Example:
                           # (r'^mywish_v1/', include('mywish_v1.foo.urls')),

                       # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
                       # to INSTALLED_APPS to enable admin documentation:
                           # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       # Uncomment the next line to enable the admin:
                           # (r'^admin/', include(admin.site.urls)),

                       (r'^$', 'mywish_v1.main.views.index'),

                       (r'^user/register$', 'mywish_v1.user_management.views.register'),
)
