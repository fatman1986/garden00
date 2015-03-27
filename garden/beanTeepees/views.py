from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def beanTeepees(request):
	return render(request, 'beanTeepees/beanTeepees.html')