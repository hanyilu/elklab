# -*- coding: utf-8 -*-
from django.db import models


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=50, default='', db_index=True)
    pwd = models.CharField(max_length=100, default='')
    status = models.SmallIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=50, default='', db_index=True)
    gender = models.SmallIntegerField(default=0)
    phone = models.CharField(max_length=20, default='')
    nick_name = models.CharField(max_length=20, default='')
    create_at = models.DateTimeField(auto_now_add=True)
