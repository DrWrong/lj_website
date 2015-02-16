# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, to='cms.CMSPlugin', parent_link=True, serialize=False, auto_created=True)),
                ('theme', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('photo', models.ImageField(upload_to='')),
                ('plugin', models.ForeignKey(to='gallery.PhotoGallery', related_name='photos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
