from django.conf.urls import patterns, include, url

from consulting import views

urlpatterns = patterns('',
	url(r'^$', views.consulting),
)