__author__ = 'amenon'

from django.conf.urls import *

from ajax_auth import views

urlpatterns = patterns('',
                       url(r'^login/$', views.LoginView.as_view(), name='ajax-auth-login'),
                       url(r'^logout/$', views.LogoutView.as_view(), name='ajax-auth-logout'),
                       url(r'^register/$', views.RegisterView.as_view(), name='ajax-auth-register'),
)
