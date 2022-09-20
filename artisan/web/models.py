from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default='avatar.jpg')
