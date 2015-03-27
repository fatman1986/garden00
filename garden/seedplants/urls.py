from django.conf.urls import patterns, include, url

from seedplants import views

urlpatterns = patterns('',
	url(r'^$', views.seedplants),
)