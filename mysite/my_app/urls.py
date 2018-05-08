
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete #login view that we can check in doc how it looks like


urlpatterns = [
	url(r'^home', views.home, name='home'),
	url(r'^login/$', login, {'template_name': 'my_app/login.html'}),#because we dont know the exact view path we enter path in such way {'template_name': 'my_app/login.html'}),
	url(r'^logout/$', logout, {'template_name': 'my_app/logout.html'}),
	url(r'^register/$', views.register, name='register'),
	url(r'^profile/$', views.view_profile, name='view_profile'),
	url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
	url(r'^change-password/$', views.change_password, name='change_password'),
	url(r'^reset-password/$', password_reset, {'template_name': 'my_app/reset_password.html'}, name='reset_password'),

	url(r'^reset-password/done/$', password_reset_done, {'template_name': 'my_app/reset_password_done.html'}, name='password_reset_done'),

	url(r'^reset-password/confirm/$', password_reset_confirm, name='password_reset_confirm'),
	# url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>,+)/$' password_reset_confirm, name='password_reset_confirm'),

	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm', {'template_name': 'my_app/reset_password_confirm.html'},
        name='password_reset_confirm'),

	url(r'^reset-password/complete/$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'my_app/reset_password_complete.html'}, name='password_reset_complete')
]	


"""
in order to create password reset and possib to gt new password via email
we need impor password_reset and password_reset_done function and then create urls in such way 
url(r'^reset-password/$', password_reset, name='reset_password'),
url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
and we will be redirected to the django reset password page


added links and variables to settings.py and launched link in the separate window python -m smtpd -n -c DebuggingServer localhost:1025
incorrect path with password reset

Нам необхідно запустити в новому вікні силку, для того щоб мати можливість надіслати 
імейл


"""