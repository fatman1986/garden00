from django.conf.urls import patterns, include, url

from beanTeepees import views

urlpatterns = patterns('',
	url(r'^$', views.beanTeepees),
)