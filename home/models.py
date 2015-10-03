from django.db import models
from django.conf import settings

class About(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()

	def __str__(self):
		return self.title	


class Member(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	position = models.CharField(max_length=200)
	biography = models.TextField()
	avatar = models.ImageField(upload_to='static/images')

	def __str__(self):
		return self.last_name

