# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='linenos',
            field=models.BooleanField(default=True, verbose_name='\u663e\u793a\u884c\u53f7'),
        ),
    ]
