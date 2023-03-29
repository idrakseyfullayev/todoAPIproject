from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    photo = models.ImageField(upload_to="photos", blank=True, null=True)
    Genders = (
        ('M', 'Man'),
        ('W', 'Woman'),
    )
    gender = models.CharField(max_length=5, choices=Genders, default='M')

    
