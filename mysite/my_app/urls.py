from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [
	url(r'^home', views.home, name='home'),
	url(r'^login/$', login, {'template_name': 'my_app/login.html'}),
	url(r'^logout/$', logout, {'template_name': 'my_app/logout.html'}),
	url(r'^register/$', views.register, name='register'),
]