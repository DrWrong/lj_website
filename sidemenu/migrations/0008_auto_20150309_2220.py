# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('sidemenu', '0007_auto_20150309_2212'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='productmenu',
        #     name='cmsplugin_ptr',
        # ),
        # migrations.RemoveField(
        #     model_name='products',
        #     name='plugin',
        # ),
        # migrations.DeleteModel(
        #     name='ProductMenu',
        # ),
        # migrations.RemoveField(
        #     model_name='products',
        #     name='productdisplay',
        # ),
        # migrations.RemoveField(
        #     model_name='products',
        #     name='publish_p',
        # ),
        migrations.RemoveField(
            model_name='products',
            name='url',
        ),
    ]
