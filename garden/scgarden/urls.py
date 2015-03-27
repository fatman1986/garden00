from django.conf.urls import patterns, include, url

from scgarden import views

urlpatterns = patterns('',
	url(r'^$', views.scgarden),
	url(r'Childrens_Garden/', views.childrensGarden),
	url(r'Accessible_Gardens/', views.accessible_Gardens),
)