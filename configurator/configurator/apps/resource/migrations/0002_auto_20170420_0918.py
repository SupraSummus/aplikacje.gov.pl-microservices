# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-20 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]