from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    phone_number = models.CharField(max_length=15, null=False, blank=True)
    #country = models.CharField(max_length=15, null=False, blank=True)
    #city = models.CharField(max_length=15, null=False, blank=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def craete_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)