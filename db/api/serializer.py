from db.models import Comment, Post, Event
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
	
        #def more_than_18(value):
        #      if value < 18:
        #          raise serializers.ValidationError('Not sufficient old, you have to have more than 18 years old')
		#age_owner = IntegerField(validators=[self.more_than_18])

		class Meta:
			fields	= '__all__'
			model 	= Event

class CommentSerializer(serializers.ModelSerializer):
		class Meta:
			fields	= '__all__'
			model 	= Comment 

class PostSerializer(serializers.ModelSerializer):
		class Meta:
			fields	= '__all__'
			model 	= Post