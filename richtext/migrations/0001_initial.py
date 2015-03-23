# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='RichText',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='cms.CMSPlugin', serialize=False, parent_link=True)),
                ('content', ckeditor.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
