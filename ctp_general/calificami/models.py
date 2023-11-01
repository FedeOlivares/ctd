from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=50) 
    content = models.TextField(max_length=750)
    datePosted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=30, default='ninguno')
    
    

    def __str__(self):
        return self.title