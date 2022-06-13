from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    title : models.CharField(max_length=200)
    text : models.TextField
    author : models.ForeignKey('User', on_delete=models.CASCADE)
    created_date : models.DateTimeField('date published') 
    published_date : models.DateTimeField('date published') 