from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _ 

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), max_length=254,unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()

    object = CustomUserManager()

    def __str__(self):
        return self.email



    


