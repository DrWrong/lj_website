# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, to='cms.CMSPlugin', auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('content', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
