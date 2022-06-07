from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    mobile=models.CharField(max_length=100,unique=True)
    address=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    serviceDetails=models.CharField(max_length=100)
    plumberDetails=models.CharField(max_length=100,default="")
    painterDetails=models.CharField(max_length=100,default="")
    electricianDetails=models.CharField(max_length=100,default="")
    carpentersDetails=models.CharField(max_length=100,default="")
    rooferDetails=models.CharField(max_length=100,default="")