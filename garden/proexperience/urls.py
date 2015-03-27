from django.conf.urls import patterns, include, url

from proexperience import views

urlpatterns = patterns('',
	url(r'^$', views.proexperience),
)