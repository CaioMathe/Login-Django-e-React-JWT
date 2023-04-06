from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_flieds):
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            **extra_flieds
        ) 
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    email = models.CharField(max_length=80, unique=True)
    username = models.CharField(max_length=45)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username