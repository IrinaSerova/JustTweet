from django.db import models
from .validators import validate_content
from django.urls import reverse
# Create your models here.
from django.conf import settings

class Tweet(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.TextField(max_length=180, validators=[validate_content])
	updated = models.DateTimeField(auto_now=True, blank=True)
	created = models.DateTimeField(auto_now_add=True,  blank=True)
	def __str__(self):
		return str(self.content)

	def get_absolute_url(self):
		return reverse('tweet:detail', kwargs={'pk': self.pk})