from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def pizzaGarden(request):
	return render(request, 'pizzaGarden/pizzaGarden.html')
