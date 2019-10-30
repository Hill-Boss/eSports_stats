from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [

    url(r'^$', views.display_home, name='display_home'),
    url(r'^register/$', views.display_create, name='display_create'),
    url(r'^dashboard/$', views.display_dash, name='landingPage'),

]
