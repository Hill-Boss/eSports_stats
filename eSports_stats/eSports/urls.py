from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView

urlpatterns = [

    url(r'^$', views.display_home, name='display_home'),
    url(r'^home/$', views.display_home, name='display_home'),
    url(r'^dashboard/$', views.display_dash, name='landingPage'),
    url(r'^viewData/$', views.display_data, name='viewData'),
    url(r'^admin/manageUsers/$', views.display_create, name='ManageUsers'),

    # url(r'^ajax/getStats/$', views.ajax_getStats, name='ajax_getStats'),
    url(r'^ajax/getGamePlayer/$', views.ajax_getGamePlayer, name='ajax_getGamePlayer'),
    url(r'^ajax/registerUser/$', views.ajax_createUser, name='display_create_user'),
    url(r'^ajax/loginUser/$', views.ajax_loginUser, name='display_login_user'),
    url(r'^ajax/logoutUser/$', views.ajax_logoutUser, name='display_logout_user'),

    url(r'^test/$', views.display_test, name='test'),
    url(r'^db_data/$', views.db_data, name='db_data'),
]
