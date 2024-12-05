from django.db import models

# Create your models here.
class Newuser(models.Model):
    username=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    password=models.CharField(max_length=10)


class Newone(models.Model):
    username=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    password=models.CharField(max_length=10)
    

    