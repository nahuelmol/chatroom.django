from django.db import models

class Event(models.Model):

        class PrivacyEvent(models.Choice):
                private = 'private'
                public  = 'public'

	name			= models.CharField(max_length=30)
	user_asociated	= models.ManyToManyField()
	date_created	= models.IntegerField()
	date_to_launch	= models.IntegerField()
	description     = models.TextField(max_length=60)
        link_to_join    = models.CharField()
        privacy         = models.charField()
        solicitudes_to_join = models.IntegerField()

class Post(models.Model):

	name			= models.CharField(max_length=30)
	user_owner	= models.ForeignField(User)
	date_created	= models.IntegerField()
	date_to_launch	= models.IntegerField()
	description		= models.TextField(max_length=60)
        likes           = models.IntegerField()
        time_shared     = models.IntegerField()
        comments        = models.OneToManyField()

class Comment(models.Model):

	name			= models.CharField(max_length=30)
	user_asociated	= models.ForeignField(User)
	date_created	= models.IntegerField()
	date_to_launch	= models.IntegerField()
	description		= models.TextField(max_length=60)
