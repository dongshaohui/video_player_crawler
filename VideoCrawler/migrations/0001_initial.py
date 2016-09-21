# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='porn_video_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.CharField(default=b'', max_length=255, verbose_name='\u4ecb\u7ecd')),
                ('link', models.CharField(default=b'', max_length=255, verbose_name='\u94fe\u63a5\u5730\u5740')),
                ('thumb', models.CharField(default=b'', max_length=255, verbose_name='\u7f29\u7565\u56fe\u5730\u5740')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
