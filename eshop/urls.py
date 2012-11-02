from django.conf.urls import patterns, include, url
from catalog.views import home
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eshop.views.home', name='home'),
    # url(r'^eshop/', include('eshop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', home.as_view()),

)
