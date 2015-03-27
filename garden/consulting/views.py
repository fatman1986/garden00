from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from mainpage.models import PageModule

# Create your views here.
def consulting(request):
	pageModule_text_list = PageModule.objects.all()
	context = {'pageModule_text_list' : pageModule_text_list,} 

	return render(request, 'consulting/consulting.html', context)

