# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lessonideal.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonideal', '0019_auto_20150108_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonidealimage',
            name='images',
            field=stdimage.models.StdImageField(upload_to=lessonideal.models.get_upload_file_name, blank=True),
            preserve_default=True,
        ),
    ]
