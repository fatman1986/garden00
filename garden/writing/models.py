from django.db import models

# Create your models here.
class Journal(models.Model):
	type_text = models.CharField(max_length=200)

	def __unicode__(self):
		return u'%s' % (self.type_text)

class Publish(models.Model):
	journal = models.ForeignKey(Journal)
	assocate_url = models.CharField(max_length=200)
	title_text = models.CharField(max_length=200)
	published_date = models.DateTimeField('published date') 

	def __unicode__(self):
		return '%s' % (self.title_text)


