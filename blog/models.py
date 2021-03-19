from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('allpost')


class Post(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length = 10000)
    post_date = models.TimeField(default = timezone.now)
    category = models.CharField(max_length=100, default="unlisted items")
    likes =models.ManyToManyField(User,related_name='blog_post')

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post =models.ForeignKey(Post,related_name="comments" ,on_delete=models.CASCADE)
    name =models.CharField(max_length=255)
    body =models.TextField()
    date_added =models.DateTimeField(default=timezone.now)
    # auto_add_now =True

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('allpost', kwargs={'pk': self.pk})

