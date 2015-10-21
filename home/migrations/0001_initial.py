# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CenterPanel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Center Panel',
            },
        ),
        migrations.CreateModel(
            name='FeaturedBox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Featured Box',
            },
        ),
        migrations.CreateModel(
            name='LeftPanel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Left Panel',
            },
        ),
    ]
