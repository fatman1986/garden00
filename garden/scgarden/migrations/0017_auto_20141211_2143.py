# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import scgarden.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('scgarden', '0016_auto_20141211_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagegallery',
            name='images',
            field=stdimage.models.StdImageField(upload_to=scgarden.models.get_upload_file_name, blank=True),
        ),
    ]
