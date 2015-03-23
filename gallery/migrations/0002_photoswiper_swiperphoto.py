# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoSwiper',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, auto_created=True, to='cms.CMSPlugin')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('config', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SwiperPhoto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to='')),
                ('plugin', models.ForeignKey(to='gallery.PhotoSwiper', related_name='photos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
