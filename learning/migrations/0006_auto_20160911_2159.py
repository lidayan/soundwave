# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0005_auto_20160911_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='code',
            field=models.TextField(default=datetime.datetime(2016, 9, 11, 13, 59, 32, 64000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='snippet',
            name='title',
            field=models.CharField(default=b'', max_length=30, verbose_name='\u683c\u5f0f\u5316\u4ee3\u7801\u884c\u7684title', blank=True),
        ),
    ]
