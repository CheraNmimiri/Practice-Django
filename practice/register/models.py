from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=16)
    email = models.EmailField(max_length=255, unique=True)