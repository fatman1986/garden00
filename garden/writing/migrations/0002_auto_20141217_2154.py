# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_text', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='publishjournal',
            name='journal',
            field=models.ForeignKey(default=1, to='writing.Journal'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publishjournal',
            name='published_date',
            field=models.DateTimeField(verbose_name=b'published date'),
        ),
    ]
