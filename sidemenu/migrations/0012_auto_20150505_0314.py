# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sidemenu', '0011_auto_20150409_0144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['order']},
        ),
    ]
