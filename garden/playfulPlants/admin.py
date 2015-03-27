from django.contrib import admin
from playfulPlants.models import Image,Category


class ImagesAdmin(admin.ModelAdmin):
	#fieldsets = [
	#	(None,				 {'fields':['image_text']}),
	#	('Date information', {'fields':['pub_date'], 'classes': ['collapse']}),
		#('Image', {'fields':['image_tag']}),
	#]
	#readonly_fields = ('image_tag',)
	#list_display = ('image_text', 'pub_date', 'image_tag',)
	list_display = ('category_text', 'pub_date', 'was_published_recently',)
	list_filter = ['pub_date']
	search_fields = ['category_text']

class ImageCollectionsAdmin(admin.ModelAdmin):
	list_display = ('image_descript', 'image_tag',)

admin.site.register(Category, ImagesAdmin)
admin.site.register(Image, ImageCollectionsAdmin)