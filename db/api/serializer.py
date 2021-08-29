from db.models import Cat, Dog, Comment, Post, Event
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		fields	= '__all__'
		model 	= Cat 