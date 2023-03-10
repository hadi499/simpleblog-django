from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # return reverse("detail", kwargs={"pk": self.pk})
        return reverse("home")
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    body = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse("detail", kwargs={"pk": self.pk})
        return reverse("home")
    


