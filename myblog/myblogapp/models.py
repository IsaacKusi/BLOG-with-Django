from django.db import models
from django.utils import timezone

# Create your models here.

class BlogPosts(models.Model):
    title = models.CharField(max_length=100)
    date_published = models.DateField(default = timezone.now(), blank=True)
    post_text = models.CharField(max_length=10000000)
