# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lessonideal.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonideal', '0006_auto_20141211_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonidealimage',
            name='images',
            field=stdimage.models.StdImageField(upload_to=lessonideal.models.get_upload_file_name, blank=True),
        ),
    ]
