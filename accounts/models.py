from django.db import models
from django.contrib.auth.models import AbstractUser
import django

# Create your models here.

class CustomUser(AbstractUser):
    # add additional fields in here
    email = models.EmailField(blank=False)
    is_staff = models.BooleanField( default=True)
    date_joined = models.DateTimeField(default=django.utils.timezone.now())
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    age = models.IntegerField(null=True)

