from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    editor = models.NullBooleanField(blank=True)
    subscriber = models.NullBooleanField(blank=True)
    card_swipe = models.CharField(max_length=30, blank=True)
    state_license = models.CharField(max_length=30, blank=True)
    employee_id = models.CharField(max_length=60, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    phone2 = models.CharField(max_length=20, blank=True)
    Address1 = models.CharField(max_length=100, blank=True)
    Address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)  # add choices
    zip_code = models.CharField(max_length=15, blank=True)
    public_profile = models.NullBooleanField(blank=True)
    gender = models.CharField(max_length=7, blank=True)
    car_make = models.CharField(max_length=60, blank=True)
    car_model = models.CharField(max_length=60, blank=True)
    car_plate = models.CharField(max_length=60, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    termination_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
