# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sidemenu', '0004_productdisplay_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='products',
            name='publish_p',
            field=models.ForeignKey(blank=True, related_name='original_p', default='', to='sidemenu.Products'),
            preserve_default=False,
        ),
    ]
