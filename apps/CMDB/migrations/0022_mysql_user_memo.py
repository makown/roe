# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-29 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMDB', '0021_auto_20181029_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysql_user',
            name='memo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u5907\u6ce8'),
        ),
    ]
