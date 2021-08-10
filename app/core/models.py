from django.db import models
from django.contrib.auth.models import UserManager , AbstractBaseUser , BaseUserManager , PermissionsMixin
from django.db.models.base import Model
from django.conf import settings


# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email : 
            raise ValueError('User must Enter Email')

        user = self.model(email=self.normalize_email(email) , **extra_fields)
        user.set_password(password)
        user.save(using = self._db)

        return user
    def create_superuser(self, email, password):
        """Creates and saves new superuser"""
        user = self.create_user(email,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser,PermissionsMixin,Model):
    email = models.EmailField(max_length=100,unique=True)
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class Tag(models.Model):
    """Tag to be used for a recipe"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name            