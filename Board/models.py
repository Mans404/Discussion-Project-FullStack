from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
# Create your models here.

class Boards(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    
    def get_posts_count(self):
        return Posts.objects.filter(topic__board = self).count()

class Topics(models.Model):
    subject = models.CharField(max_length=100)
    board   = models.ForeignKey(Boards,related_name='topics',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.subject
    


    def get_posts_count(self):
        return self.posts.count()  # Assuming you have a related_name='posts' on your Posts model


class Posts(models.Model):
    message = models.TextField(max_length=100)
    topic   = models.ForeignKey(Topics,related_name='posts',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)


