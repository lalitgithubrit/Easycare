from django.db import models

# Create your models here.

class Account(models.Model):
    Patient_name=models.CharField(max_length=20)
    Contact_No=models.IntegerField()
    DOB=models.IntegerField()
    Address=models.CharField(max_length=100)

class Emergency(models.Model):
    Ambulance_No=models.IntegerField()
    Family_No=models.IntegerField()

class Pharmacy2(models.Model):
    Diseases2=models.CharField(max_length=50)
    Medicine2=models.CharField(max_length=50)

