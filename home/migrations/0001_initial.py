# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('featured_box_heading', models.CharField(help_text=b'The heading of the featured box', max_length=200)),
                ('featured_box_content', models.CharField(help_text=b'The text for the featured box', max_length=200)),
                ('featured_box_link', models.CharField(default=b'The url where the featured box links to', max_length=200)),
                ('left_panel', mezzanine.core.fields.RichTextField(help_text=b'The content for the left panel', null=True, blank=True)),
                ('center_panel', mezzanine.core.fields.RichTextField(help_text=b'The content for the center panel', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Home page',
                'verbose_name_plural': 'Home pages',
            },
        ),
    ]
