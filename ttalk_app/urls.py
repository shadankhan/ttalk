from django.conf.urls import include, url
from ttalk_app import views

urlpatterns = [
		url(r'^create', views.create_profile, name='create_profile'),
		

]