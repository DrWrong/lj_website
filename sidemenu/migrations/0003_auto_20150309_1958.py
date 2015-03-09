# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('sidemenu', '0002_auto_20150309_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDisplay',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', primary_key=True, serialize=False, auto_created=True, parent_link=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='productdisplay',
            field=models.ForeignKey(to='sidemenu.ProductDisplay', default=0, blank=True, related_name='products'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='plugin',
            field=models.ForeignKey(to='sidemenu.ProductMenu', blank=True, related_name='products'),
            preserve_default=True,
        ),
    ]
