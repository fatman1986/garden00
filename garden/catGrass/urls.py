from django.conf.urls import patterns, include, url

from catGrass import views

urlpatterns = patterns('',
	url(r'^$', views.catGrass),
)