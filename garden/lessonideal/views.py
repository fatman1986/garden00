from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from mainpage.models import PageModule
from lessonideal.models import LessonIdealImage

# Create your views here.
def lessonideal(request):
	pageModule_text_list = PageModule.objects.all()
	image_context = LessonIdealImage.objects.all()
	context = {'pageModule_text_list' : pageModule_text_list, 'image_context' : image_context,} 

	return render(request, 'lessonideal/lessonideal.html', context)
