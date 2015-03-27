# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0002_auto_20141217_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assocate_url', models.CharField(max_length=200)),
                ('title_text', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(verbose_name=b'published date')),
                ('journal', models.ForeignKey(to='writing.Journal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='publishjournal',
            name='journal',
        ),
        migrations.DeleteModel(
            name='PublishJournal',
        ),
    ]
