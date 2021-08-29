from django.db import models

class Event(models.Model):

	name			= models.CharField(max_length=30)
	user_asociated	= models.ManyToManyField()
	date_created	= models.IntegerField()
	date_to_launch	= models.IntegerField()
	description		= models.TextField(max_length=60)

