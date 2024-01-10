from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    phone = models.CharField(max_length=10, null=True)
    images = models.ImageField(default="avt.jpg", upload_to ='static/images/')
    status = models.BooleanField(default=True)  # False la khong hoat ong