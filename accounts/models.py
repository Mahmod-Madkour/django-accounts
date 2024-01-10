from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
User:
    username
    password
    first_name
    last_name
    email

"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=15, null=False, blank=True)
    last_name = models.CharField(max_length=15, null=False, blank=True)
    email = models.CharField(max_length=15, null=False, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return str(self.user)