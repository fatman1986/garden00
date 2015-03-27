# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import playfulPlants.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('playfulPlants', '0002_auto_20141124_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_descript', models.CharField(max_length=200)),
                ('images', stdimage.models.StdImageField(upload_to=playfulPlants.models.get_upload_file_name, blank=True)),
                ('category', models.ForeignKey(to='playfulPlants.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='imagecollections',
            name='category',
        ),
        migrations.DeleteModel(
            name='ImageCollections',
        ),
    ]
