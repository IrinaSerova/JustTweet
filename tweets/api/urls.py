from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
    TweetListAPIView,
  

    )

urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='list'), 
    # url(r'^create/$', TweetCreateAPIView.as_view(), name='create'), # /tweet/create/
    # url(r'^(?P<pk>\d+)/$', TweetDetailAPIView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name='like-toggle'),
    # url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'), #/api/tweet/id/tweet/
]