from django.db import models

# Create your models here.

class Plumber(models.Model):
    plname=models.CharField(max_length=100)
    plnemail=models.EmailField(max_length=100,unique=True)
    plnmobile=models.CharField(max_length=10,unique=True)
    plnaddress=models.CharField(max_length=200)
    plnprice=models.CharField(max_length=10000)
    plnstatus=models.BooleanField()
    plnbook=models.BooleanField()
    plnusers=models.CharField(max_length=100);
    plntype=models.CharField(max_length=100,default="Plumber")

class Ruffer(models.Model):
    rufname=models.CharField(max_length=100)
    rufemail=models.EmailField(max_length=100,unique=True)
    rufmobile=models.CharField(max_length=10,unique=True)
    rufaddress=models.CharField(max_length=200)
    rufprice=models.CharField(max_length=10000)
    rufstatus=models.BooleanField()
    rufbook=models.BooleanField()
    rufusers=models.CharField(max_length=100);
    ruftype=models.CharField(max_length=100,default="Roofer")

class Carpenter(models.Model):
    carname=models.CharField(max_length=100)
    caremail=models.EmailField(max_length=100,unique=True)
    carmobile=models.CharField(max_length=10,unique=True)
    caraddress=models.CharField(max_length=200)
    carprice=models.CharField(max_length=10000)
    carstatus=models.BooleanField()
    carbook=models.BooleanField()
    carusers=models.CharField(max_length=100)
    cartype=models.CharField(max_length=100,default="Carpenter")
    
class Electrician(models.Model):
    elename=models.CharField(max_length=100)
    eleemail=models.EmailField(max_length=100,unique=True)
    elemobile=models.CharField(max_length=10,unique=True)
    eleaddress=models.CharField(max_length=200)
    eleprice=models.CharField(max_length=10000)
    elestatus=models.BooleanField()
    elebook=models.BooleanField()
    eleusers=models.CharField(max_length=100);
    eletype=models.CharField(max_length=100,default="Electrician")
    
class Painter(models.Model):
    painame=models.CharField(max_length=100)
    paiemail=models.EmailField(max_length=100,unique=True)
    paimobile=models.CharField(max_length=10,unique=True)
    paiaddress=models.CharField(max_length=200)
    paiprice=models.CharField(max_length=10000)
    paistatus=models.BooleanField()
    paibook=models.BooleanField()
    paiusers=models.CharField(max_length=100);
    paitype=models.CharField(max_length=100,default="Painter")