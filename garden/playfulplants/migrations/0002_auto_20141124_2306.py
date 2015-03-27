# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import playfulPlants.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('playfulPlants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagecollections',
            old_name='cateory',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='imagecollections',
            name='images',
            field=stdimage.models.StdImageField(upload_to=playfulPlants.models.get_upload_file_name, blank=True),
        ),
    ]
