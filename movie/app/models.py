from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomerUser(AbstractUser):
    rank = models.CharField(max_length=5)
    phone_number = models.TextField()
