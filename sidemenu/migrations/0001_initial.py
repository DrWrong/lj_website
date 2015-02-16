# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMenu',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=20)),
                ('plugin', models.ForeignKey(related_name='products', to='sidemenu.ProductMenu')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
