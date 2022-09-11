from django.db import models
# Create your models here.

class user(models.Model):   
    username = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=100, null=True)
    date_created  = models.DateField(auto_now_add=True, null=True)

        