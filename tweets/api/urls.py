from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import (
	TweetListAPIView,
	TweetCreateAPIView
	# TweetListView, 
	# TweetDetailView, 
	# TweetCreateView, 
	# TweetUpdateView, 
	# TweetDeleteView
	)

urlpatterns = [
	url(r'^$', TweetListAPIView.as_view(), name='list'),
	url(r'^create/$', TweetCreateAPIView.as_view(), name='create'),
    # url(r'^$', TweetListView.as_view(), name="list"), # localhost:4000/tweet/
    # url(r'^create/$', TweetCreateView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # localhost:4000/tweet/id_of_tweet
]
