from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager

from utils.models import BaseModel
# Create your models here.

class User(AbstractUser,BaseModel):

    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    def __str__(self):
        return self.email

