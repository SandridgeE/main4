from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.loginscreen, name='dashboard'),
	url(r'^register$', views.register, name='register'),
	url(r'^login$',views.login, name='login'),
	url(r'^success$', views.success, name='landing'),

]