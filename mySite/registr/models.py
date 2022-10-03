from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
