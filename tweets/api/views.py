from tweets.models import Tweet

from .serializers import ModelTweetSerializer
from rest_framework import generics

class TweetListAPIView(generics.ListAPIView):
    serializer_class = ModelTweetSerializer
    queryset = Tweet.objects.all()

   