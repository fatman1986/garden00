# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lessonideal.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LessonIdealImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('images', stdimage.models.StdImageField(upload_to=lessonideal.models.get_upload_file_name, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
