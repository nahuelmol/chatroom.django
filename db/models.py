from django.db import models
from django.contrib.auth.models import User

class Chatroom(models.Model):
	chatroom_name 	= models.CharField(max_length=30)
	creation_date  	= models.CharField(max_length=30)
	author			= models.CharField(max_length=30)
	link_to_join 	= models.CharField(max_length=30) 	

	asunto 			= models.CharField(	max_length=30,
										default='conversation')
	description 	= models.TextField(	max_length=60,
										default='a normal conversation')

	def __str__(self):
		return 'Nothing'

class Encuesta(models.Model):

	date_created		= models.DateField()
	deadline 			= models.DateField()

	user_creator 		= models.ForeignKey(User, on_delete=models.CASCADE)
	options				= models.IntegerField()
	vote_count 			= models.IntegerField()

class Follower(models.Model):

	date_follow			= models.DateField()
	user_follower 		= models.ForeignKey(User, on_delete=models.CASCADE)
	#followed_user		= models.ForeignKey(User, on_delete=models.CASCADE)
	followed_chatroom	= models.ForeignKey(Chatroom, on_delete=models.CASCADE)

class Subscriber(models.Model):

	date_subs			= models.DateField()
	subscribed_user		= models.ForeignKey(User, on_delete=models.CASCADE)
	follower_subscriber	= models.ForeignKey(Follower, on_delete=models.CASCADE)
	
class Moderator(models.Model):

	user_moderator	= models.ForeignKey(User, on_delete=models.CASCADE)
	date_conversion	= models.DateField()
	


class Event(models.Model):

	class PrivacyEvent(models.TextChoices):
		private = 'private'
		public  = 'public'

	name				= models.CharField(max_length=30)

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

	

class Message(models.Model):
	chatroom_id 	= models.ForeignKey(Chatroom, on_delete=models.CASCADE, null=True)
	author			= models.CharField(max_length=30)
	content 		= models.TextField(max_length=30)
	creation_date 	= models.CharField(max_length=30)
	chatroom 		= models.CharField(max_length=30)

