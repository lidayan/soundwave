# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0003_snippet_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='style',
            field=models.CharField(default=b'default', max_length=30, verbose_name='\u683c\u5f0f\u5316\u4ee3\u7801\u7684style', blank=True),
        ),
    ]
