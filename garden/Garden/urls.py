from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Garden.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^my_blog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^Blog/', include('zinnia.urls', namespace='zinnia')),
	url(r'^comments/', include('django_comments.urls')),
    url(r'^$', include('mainpage.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('mainpage.urls')),
    url(r'^garden_show/', include('scgarden.urls')),
    url(r'^school_and_children_garden_link/', include('scgarden.urls')),
    url(r'^garden_resource/', include('playfulPlants.urls')),
    url(r'^playful_plants/', include('playfulPlants.urls')),
    url(r'^books/', include('books.urls')),
    url(r'^seed_and_plant/', include('seedplants.urls')),   
    url(r'^lesson_ideal/', include('lessonideal.urls')),
    url(r'^consulting/', include('consulting.urls')),
    url(r'^contact_me/', include('consulting.urls')),
    url(r'^writing/', include('writing.urls')),
    url(r'^about_me/', include('writing.urls')),       
    url(r'^professional_experience/', include('proexperience.urls')),
    url(r'^in_the_press/', include('press.urls')),
    url(r'^Bean_Teepees/', include('beanTeepees.urls')),
    url(r'^Cat_Grass/', include('catGrass.urls')),
    url(r'^Pizza_Garden/', include('pizzaGarden.urls')),
    url(r'^Seed_Balls/', include('seedBalls.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
)
