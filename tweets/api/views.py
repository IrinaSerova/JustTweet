from tweets.models import Tweet
from django.db.models import Q
from rest_framework import permissions

from .serializers import ModelTweetSerializer
from rest_framework import generics

class TweetListAPIView(generics.ListAPIView):
    serializer_class = ModelTweetSerializer
    

    def get_queryset(self, *args, **kwargs):
    	qs = Tweet.objects.all()
    	print(self.request.GET)
    	query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                    )
        return qs

class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = ModelTweetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




    	# requested_user = self.kwargs.get("username")

    	# if requested_user:
    	# 	qs = Tweet.objects.filter(user__username=requested_user).order_by("-timestamp")
    	# else:
     #        im_following = self.request.user.profile.get_following() # none
     #        qs1 = Tweet.objects.filter(user__in=im_following)
     #        qs2 = Tweet.objects.filter(user=self.request.user)
     #        qs = (qs1 | qs2).distinct().order_by("-timestamp")

     #        query = self.request.GET.get("q", None)
     #        if query is not None:
     #        	qs = qs.filter(
     #        		Q(content__icontains=query) |
     #        		Q(user__username__icontains=query)
     #        		)
     #        	return qs



   