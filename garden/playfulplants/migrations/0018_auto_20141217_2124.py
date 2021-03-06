# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import playfulPlants.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('playfulPlants', '0017_auto_20141217_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='images',
            field=stdimage.models.StdImageField(upload_to=playfulPlants.models.get_upload_file_name, blank=True),
        ),
    ]
