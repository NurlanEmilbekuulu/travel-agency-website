from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^login/$', views.login_view, name='login'),
	url(r'^register/$', views.register_view, name='register'),
]
