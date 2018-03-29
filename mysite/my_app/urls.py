from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
	url(r'^home', views.home, name='home'),
	url(r'^login/$', login, {'template_name': 'my_app/login.html'}),
]