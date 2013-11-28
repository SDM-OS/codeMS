import datetime
from django.db import models

class Category(models.Model):
	title = models.CharField(max_length=250)
	slug  = models.SlugField(unique_for_date='pub_date')
	description = models.TextField()

class Entry(models.Model):
	title = models.CharField(max_length=250)
	excerpt = models.TextField(blank=True)
	body = models.TextField()
	pub_date = models.DateTimeField(default=datetime.datetime.now)

	def __unicode__(self):
		return self.title
		