# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sidemenu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='url',
            field=models.CharField(max_length=256),
            preserve_default=True,
        ),
    ]
