from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def catGrass(request):
	return render(request, 'catGrass/catGrass.html')