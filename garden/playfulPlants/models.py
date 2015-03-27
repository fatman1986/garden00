import datetime
from django.db import models
from time import time
from stdimage import StdImageField
from django.utils import timezone

def get_upload_file_name(instance, filename):
	return

class Category(models.Model):
	category_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
 	# search_fields = ['question_text']
 	was_published_recently.admin_order_field = 'pub_date'
 	was_published_recently.boolean = True
 	was_published_recently.short_description = 'published recently?'

 	def __unicode__(self):
		return u'%s %s' % (self.category_text, self.pub_date)
 		
class Image(models.Model):
	category = models.ForeignKey(Category)
	image_descript = models.CharField(max_length=200)
	
	def get_upload_file_name(instance, filename):
		return "upload_files/%s_%s" % (str(time()).replace('.','_'), filename)
	images = StdImageField(upload_to=get_upload_file_name, blank=True, variations={'large': (400, 400), 'thumbnail': (100, 100, True)})
	def image_tag(self):
		return u'<img src="%s" />' % self.images.thumbnail.url
	image_tag.short_description = 'Image'
	image_tag.allow_tags = True

	def __unicode__(self):
		return '%s' % (self.image_descript)
