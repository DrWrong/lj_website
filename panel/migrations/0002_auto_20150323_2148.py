# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
    ]
