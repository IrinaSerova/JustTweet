from rest_framework import generics, permissions
from django.db.models import Q
from tweets.models import Tweet
from .serializers import ModelTweetSerializer

class TweetListAPIView(generics.ListAPIView):
	serializer_class = ModelTweetSerializer
	
	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all()
		# .order_by("-created")
		print(self.request.GET)
		query = self.request.GET.get('query', None)
		if query is not None:
			qs = qs.filter(Q(content__icontains=query) | Q(user__username__icontains=query))
		return qs

class TweetCreateAPIView(generics.CreateAPIView):
	serializer_class = ModelTweetSerializer
	permission_class = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)