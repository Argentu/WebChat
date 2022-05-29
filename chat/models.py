from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from hashlib import sha1
from datetime import datetime


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=10, unique=True, db_index=True)
    password = models.TextField()

    USERNAME_FIELD = 'username'
    objects = UserManager()


class Chatroom(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    invite_link = models.TextField()
    Log_file = models.FileField()
    Users = models.ManyToManyField(MyUser)
