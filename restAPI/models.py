from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.

class User_new(AbstractBaseUser):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=600)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']

class Advisor(models.Model):
    name = models.CharField(max_length=60)
    photo_url = models.URLField()

class Booking(models.Model):
    booking_time = models.DateTimeField()
    user = models.ForeignKey(User_new, on_delete=models.CASCADE)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
