from django.db import models

# Create your models here.

class Author(models.Model):
    first_name    = models.CharField(max_length=30)
    second_name   = models.CharField(max_length=30, blank=True)
    last_name     = models.CharField(max_length=30)

    email         = models.EmailField(max_length=30, default="me@myself.com")
    twitter_name  = models.CharField(max_length=50, blank=True)
    facebook_name = models.CharField(max_length=50, blank=True)

    registered    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Post(models.Model):
    title   = models.CharField(max_length=50)
    content = models.TextField()
    author  = models.ForeignKey(Author, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/', max_length=100, blank=True)

    posted  = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    notes   = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.title