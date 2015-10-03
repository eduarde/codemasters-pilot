from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.welcome_home, name='welcome_home'),
]