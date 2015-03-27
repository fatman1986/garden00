from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from mainpage.models import PageModule
from scgarden.models import ImageGallery
# Create your views here.
def scgarden(request):
	pageModule_text_list = PageModule.objects.all()
	image_gallery_context = ImageGallery.objects.all()
	first_image = get_object_or_404(ImageGallery, pk=4)
	context = {'pageModule_text_list' : pageModule_text_list, 'image_gallery_context' : image_gallery_context, 'first_image' : first_image,} 

	return render(request, 'scgarden/scgarden.html', context)

def childrensGarden(request):
	pageModule_text_list = PageModule.objects.all()
	context = {'pageModule_text_list' : pageModule_text_list,}

	return render(request, 'scgarden/childrensGarden.html', context)

def accessible_Gardens(request):
	pageModule_text_list = PageModule.objects.all()
	context = {'pageModule_text_list' : pageModule_text_list,}

	return render(request, 'scgarden/accessible_Gardens.html', context)
