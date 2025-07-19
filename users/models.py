from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("restaurant", "Restaurant"),
        ("allergist", "Allergist"),
        ("patient", "Patient"),
    ]


    role = models.CharField(choices= ROLE_CHOICES, max_length=255)