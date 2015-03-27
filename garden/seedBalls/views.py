from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def seedBalls(request):
	return render(request, 'seedBalls/seedBalls.html')