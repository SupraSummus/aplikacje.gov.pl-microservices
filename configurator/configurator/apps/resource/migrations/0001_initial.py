# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-19 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DictResourceEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DictResource',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resource.Resource')),
            ],
            options={
                'abstract': False,
            },
            bases=('resource.resource',),
        ),
        migrations.CreateModel(
            name='IntResource',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resource.Resource')),
                ('value', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('resource.resource',),
        ),
        migrations.CreateModel(
            name='ListResource',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resource.Resource')),
            ],
            options={
                'abstract': False,
            },
            bases=('resource.resource',),
        ),
        migrations.CreateModel(
            name='StringResource',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resource.Resource')),
                ('value', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('resource.resource',),
        ),
        migrations.AddField(
            model_name='resource',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_resource.resource_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='dictresourceentry',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resource.Resource'),
        ),
        migrations.AddField(
            model_name='listresource',
            name='value',
            field=models.ManyToManyField(related_name='member_of_lists', to='resource.Resource'),
        ),
        migrations.AddField(
            model_name='dictresourceentry',
            name='dictionary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='resource.DictResource'),
        ),
    ]
