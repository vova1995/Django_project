from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [
	url(r'^home', views.home, name='home'),
	url(r'^login/$', login, {'template_name': 'my_app/login.html'}),
	url(r'^logout/$', logout, {'template_name': 'my_app/logout.html'}),
	url(r'^register/$', views.register, name='register'),
	url(r'^profile/$', views.view_profile, name='view_profile'),
	url(r'^profile/edit/$', views.edit_profile, name='edit_profile')
]