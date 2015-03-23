# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('sidemenu', '0009_auto_20150309_2222'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='productmenu',
        #     name='cmsplugin_ptr',
        # ),
        migrations.DeleteModel(
            name='ProductMenu',
        ),
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
    ]
