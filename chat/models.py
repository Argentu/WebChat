from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=10, unique=True, db_index=True)
    password = models.TextField()

    USERNAME_FIELD = 'username'
    objects = UserManager()

'''
class Chatroom(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    owner_name = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    invite_link = None
    Log_file = None'''

'''
class Message(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    text = models.CharField(max_length=255)'''