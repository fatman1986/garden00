from django.conf.urls import patterns, include, url

from press import views

urlpatterns = patterns('',
	url(r'^$', views.press),
)