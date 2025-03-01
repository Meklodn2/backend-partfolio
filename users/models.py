from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.username
        
    