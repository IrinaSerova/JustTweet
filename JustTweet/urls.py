"""JustTweet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from django.conf.urls import url, include

from .views import home
from tweets.views import TweetListView
from accounts.views import UserRegisterView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view(), name='home'),
    url(r'^tweet/', include(('tweets.urls', 'tweet'), namespace='tweet')),
    url(r'^tweet/api/', include(('tweets.api.urls', 'tweet-api'), namespace='tweet-api')),
    url(r'^register/$', UserRegisterView.as_view(), name='register'),
]
