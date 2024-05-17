from django.db import models

class LoginModel(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
# Create your models here.
