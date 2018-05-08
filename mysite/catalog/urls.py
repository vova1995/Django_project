from django.conf.urls import url

from . import views


app_name = 'catalog'#this variable shows the name of our app if u can see it is ccatalog
urlpatterns = [
	url(r'^$', views.catalog_home, name='home'),
	url(r'^(?P<catalog_id>[0-9]+)$', views.catalog_detail, name='detail'),
	]

""" views.catalog_detail consist off:
views - it is views.py where we create our views dunctions
catalog_detail - it is function in views
name=catalog_detail or in our situation we have basic bariabl catalog that s why we can name just detail"""