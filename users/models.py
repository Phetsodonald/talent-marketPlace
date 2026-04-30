from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICE = (
        ('organizer', 'organizer'),
        ('talent', 'talent'),
        ('admin', 'admin'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICE)
    phone = models.CharField(max_length=20, blank=True, null=True)