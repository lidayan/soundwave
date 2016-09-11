# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_auto_20160911_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 9, 11, 10, 51, 3, 570000, tzinfo=utc), max_length=30, verbose_name='\u683c\u5f0f\u5316\u4ee3\u7801\u884c\u7684title'),
            preserve_default=False,
        ),
    ]
