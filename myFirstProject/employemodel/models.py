from django.db import models


class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)# Create your models here.
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
