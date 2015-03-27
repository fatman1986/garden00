from django.conf.urls import patterns, include, url

from pizzaGarden import views

urlpatterns = patterns('',
	url(r'^$', views.pizzaGarden),
)