# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(db_index=True, default=b'', max_length=50)),
                ('pwd', models.CharField(default=b'', max_length=100)),
                ('status', models.SmallIntegerField(default=0)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(db_index=True, default=b'', max_length=50)),
                ('gender', models.SmallIntegerField(default=0)),
                ('phone', models.CharField(default=b'', max_length=20)),
                ('nick_name', models.CharField(default=b'', max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
