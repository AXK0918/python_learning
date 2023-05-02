from django.db import models

# Create your models here.

class Meta:
        app_label = 'first_app'
class Name(models.Model):
    name = models.CharField(max_length=255)
    

class ID(models.Model):
    id_number = models.IntegerField(max_length=10)

class Contact(models.Model):
    phone = models.CharField(max_length=20)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)

