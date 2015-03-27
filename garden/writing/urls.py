from django.conf.urls import patterns, include, url

from writing import views

urlpatterns = patterns('',
	url(r'^$', views.writing),
)