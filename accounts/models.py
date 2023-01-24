from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField(unique=True)


# class FriendShip(models.Model):
