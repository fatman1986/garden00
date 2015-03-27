# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import stdimage.models
import lessonideal.models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonideal', '0002_auto_20141211_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonidealimage',
            name='url_text',
            field=models.CharField(default=datetime.date(2014, 12, 11), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lessonidealimage',
            name='images',
            field=stdimage.models.StdImageField(upload_to=lessonideal.models.get_upload_file_name, blank=True),
        ),
    ]
