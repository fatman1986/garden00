# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import stdimage.models
import scgarden.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scgarden', '0029_auto_20141221_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagegallery',
            name='url_text',
            field=models.CharField(default=datetime.datetime(2015, 1, 9, 1, 21, 6, 489185, tzinfo=utc), max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='images',
            field=stdimage.models.StdImageField(upload_to=scgarden.models.get_upload_file_name, blank=True),
            preserve_default=True,
        ),
    ]
