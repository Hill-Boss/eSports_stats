from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView

urlpatterns = [

    url(r'^$', views.display_home, name='display_home'),
    url(r'^register/$', views.display_create, name='display_create'),
    url(r'^dashboard/$', views.display_dash, name='landingPage'),
    url(r'^test/$', views.display_test, name='test'),
    url(r'^db_data/$', views.db_data, name='db_data'),
    url(r'^viewData/$', views.display_data, name='viewData'),
    url(r'^ajax/getStats/$', views.ajax_getStats, name='ajax_getStats'),
    url(r'^ajax/getGamePlayer/$', views.ajax_getGamePlayer, name='ajax_getGamePlayer'),
    
    # url(r'^home/$', views.display_test_home, name='home'),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login/login.html'), name='login'),
# views.display_login, name='login'

]
