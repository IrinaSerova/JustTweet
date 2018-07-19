from rest_framework import serializers
from tweets.models import Tweet
from accounts.api.serializers import UserDisplaySerializer
from django.utils.timesince import timesince


class ModelTweetSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer(read_only=True)
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	
	class Meta:
		model = Tweet
		fields = ['user', 'content', 'created', 'date_display', 'timesince']

	def get_date_display(self, obj):
		return obj.created.strftime("%b %e, %Y at %I:%M %p")

	def get_timesince(self, obj):
		return timesince(obj.created) + " ago"