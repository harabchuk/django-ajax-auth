from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^ajax_auth/', include('ajax_auth.urls')),
    url(r'^', include('ajax_auth_test.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
