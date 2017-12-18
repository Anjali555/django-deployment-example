from django.db import models

# Create your models here.
class Registration(models.Model):
    Fullname = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)
    contact = models.CharField(max_length=25)

class Newsletter(models.Model):
    email1 = models.EmailField(max_length=254,unique=True)
