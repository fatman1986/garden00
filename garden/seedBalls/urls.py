from django.conf.urls import patterns, include, url

from seedBalls import views

urlpatterns = patterns('',
	url(r'^$', views.seedBalls),
)