from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from mainpage.models import PageModule
from playfulPlants.models import Category

# Create your views here.
def playfulPlants(request):
	pageModule_text_list = PageModule.objects.all()
	category = Category.objects.all()
	context = {'pageModule_text_list' : pageModule_text_list, 'category' : category,} 
	
	return render(request, 'playfulPlants/playfulPlants.html', context)

