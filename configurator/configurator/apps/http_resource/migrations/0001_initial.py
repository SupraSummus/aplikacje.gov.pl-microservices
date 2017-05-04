# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-20 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application', '0001_initial'),
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HTTPResource',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resource.Resource')),
                ('api', models.CharField(blank=True, max_length=200)),
                ('host', models.CharField(max_length=200)),
                ('port', models.IntegerField()),
                ('path', models.CharField(max_length=1000)),
                ('app', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.AppResource')),
            ],
            options={
                'abstract': False,
            },
            bases=('resource.resource',),
        ),
    ]