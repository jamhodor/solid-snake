from django.db import models
from django.utils import timezone

from tinymce import models as tinymce_models

# Create your models here.

class Author(models.Model):
    first_name    = models.CharField(max_length=30)
    last_name     = models.CharField(max_length=30)

    email         = models.EmailField(max_length=30, default="me@myself.com")
    twitter_name  = models.CharField(max_length=50, blank=True)
    facebook_name = models.CharField(max_length=50, blank=True)

    registered_on    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Post(models.Model):
    title   = models.CharField(max_length=150)
    title_picture = models.ImageField(upload_to='images/blog/', max_length=60, blank=True)

    content = tinymce_models.HTMLField()

    author  = models.ForeignKey(Author, on_delete=models.CASCADE)

    posted_on  = models.DateTimeField(default=timezone.localtime)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Picture(models.Model):
    caption      = models.CharField(max_length=100)
    post_picture = models.ImageField(upload_to='images/blog/', max_length=60, blank=True)
    post         = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

class Event(models.Model):
    title             = models.CharField(max_length=100)
    event_description = models.CharField(max_length=200, blank=True)
    event_picture     = models.ImageField(upload_to='images/blog/', max_length=60, blank=True)
    link_url          = models.URLField(blank=True)

    posted_on = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return self.title