from django.test import TestCase
from .models import Tweet
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()



class TweetModelTestCase(TestCase):

    def setUp(self):
        test_user = User.objects.create(username='Tester')

    def test_tweet(self):
        obj = Tweet.objects.create(
                user= User.objects.first(),
                content='Test content'
            )
        self.assertTrue(obj.content == "Test content")
        self.assertTrue(obj.id == 1)
        absolute_url = reverse("tweet:detail", kwargs={"pk": 1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)

    def test_tweet_url(self):
        obj = Tweet.objects.create(
                user= User.objects.first(),
                content='Test content'
            )
        absolute_url = reverse("tweet:detail", kwargs={"pk": obj.pk})
        self.assertEqual(obj.get_absolute_url(), absolute_url)

