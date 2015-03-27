# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=60)),
                ('content', ckeditor.fields.RichTextField()),
                ('abstract', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
    ]
