from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from .managers import UserManager

# Create your models here.

class User(AbstractUser): 
    username = None
    email = models.EmailField(verbose_name='email', unique=True, blank=False,null=False)
    is_company = models.BooleanField(default=False)
    is_seeker = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
        




