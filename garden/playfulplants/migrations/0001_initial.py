# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import playfulPlants.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageCollections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_descript', models.CharField(max_length=200)),
                ('images', stdimage.models.StdImageField(upload_to=playfulPlants.models.get_upload_file_name, blank=True)),
                ('cateory', models.ForeignKey(to='playfulPlants.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
