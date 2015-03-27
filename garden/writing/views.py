from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
import feedparser
from mainpage.models import PageModule
from writing.models import Journal
from writing.RssObj import RssObject
import time

# Create your views here.
def writing(request):
	RssObjList = []
	pageModule_text_list = PageModule.objects.all()
	journal_list = Journal.objects.all() 
	feeds = feedparser.parse('http://www.thecolumbiastar.com/news.xml')
	for entry in feeds.entries:
		if 'Home_%28and%29_Garden' in entry.link:
			timeValue = time.asctime(entry.published_parsed)
			newRssObj = RssObject(timeValue, entry.title, entry.link)
			RssObjList.append(newRssObj)

	context = {'pageModule_text_list' : pageModule_text_list,'journal_list' : journal_list, 'RssObj' : RssObjList,}

	return render(request, 'writing/writing.html', context)

	