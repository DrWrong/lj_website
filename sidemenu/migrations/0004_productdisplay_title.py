# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sidemenu', '0003_auto_20150309_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdisplay',
            name='title',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
