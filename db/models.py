from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):

	class PrivacyEvent(models.TextChoices):
		private = 'private'
		public  = 'public'

	name				= models.CharField(max_length=30)

	#user_asociated		= models.ManyToManyField(User)
	#user_owner_creator	= models.ForeignKey(User, on_delete=models.CASCADE)

	date_created		= models.IntegerField()
	date_to_launch		= models.IntegerField()

	description     	= models.TextField(max_length=60)
	link_to_join    	= models.CharField(max_length=30)
	solicitudes_to_join = models.IntegerField()
	privacy         	= models.CharField(	max_length=40,
											choices=PrivacyEvent.choices,
											blank=None,
											default='unknown')

class Post(models.Model):

	name			= models.CharField(max_length=30)
	user_owner		= models.ForeignKey(User, on_delete=models.CASCADE)
	date_created	= models.IntegerField()
	date_to_launch	= models.IntegerField()
	description		= models.TextField(max_length=60)
	likes           = models.IntegerField()
	time_shared     = models.IntegerField()

class Comment(models.Model):

	name			= models.CharField(max_length=30)
	user_owner		= models.ForeignKey(User, on_delete=models.CASCADE)
	date_created	= models.IntegerField()
	date_to_launch	= models.IntegerField()
	description		= models.TextField(max_length=60)
	post 			= models.ForeignKey(Post, on_delete=models.CASCADE)