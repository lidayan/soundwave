# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0004_snippet_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='title',
            field=models.CharField(max_length=30, verbose_name='\u683c\u5f0f\u5316\u4ee3\u7801\u884c\u7684title', blank=True),
        ),
    ]
