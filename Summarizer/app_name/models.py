from django.db import models

# Create your models here.
class details(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subscription = models.BooleanField()
    ip = models.GenericIPAddressField()

class image(models.Model):
    name=models.IntegerField()
    image1=models.ImageField(upload_to='images/')