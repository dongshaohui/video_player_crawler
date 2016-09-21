# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VideoCrawler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='porn_video_info',
            name='number',
            field=models.IntegerField(default=0, verbose_name='\u7f16\u53f7'),
            preserve_default=True,
        ),
    ]
