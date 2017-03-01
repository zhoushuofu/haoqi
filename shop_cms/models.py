# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class UserInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    sex = models.IntegerField()
    status = models.IntegerField()
    rank = models.IntegerField()
    new_rank = models.IntegerField()
    day = models.IntegerField()
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    phone = models.CharField(max_length=16)
    province = models.CharField(max_length=16)
    nick = models.CharField(max_length=32)
    passwd = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    area = models.CharField(max_length=32)
    source = models.CharField(max_length=32)
    head = models.CharField(max_length=128)
    ip = models.CharField(max_length=16)
    love_sports = models.CharField(max_length=64)
    signature = models.CharField(max_length=256)
    ts = models.DateTimeField()
    reg_ts = models.DateTimeField()
    phone_type = models.CharField(max_length=64)
    os = models.CharField(max_length=64)
    ver = models.CharField(max_length=16)
    now_ver = models.CharField(max_length=16)
    device_id = models.CharField(max_length=128)
    channel = models.CharField(max_length=64, blank=True, null=True)
    last_login_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_info'

