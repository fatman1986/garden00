from django.conf.urls import patterns, include, url

from lessonideal import views

urlpatterns = patterns('',
	url(r'^$', views.lessonideal),
)