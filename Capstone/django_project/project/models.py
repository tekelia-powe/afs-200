from typing import Text
from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.

class Contact(models.Model):
    
    fname= models.CharField(max_length=200, null=True)
    lname= models.CharField(max_length=200, null=True)
    phone= models.CharField(max_length=200, null=True)
    email= models.EmailField(max_length=200, null=True)
    address= models.CharField(max_length=200, null=True)
    address2= models.CharField(max_length=200, null=True)
    city= models.CharField(max_length=200, null=True)
    state= models.CharField(max_length=200, null=True)
    zip= models.CharField(max_length=200, null=True)
    