# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('highlighted', models.TextField()),
                ('language', models.CharField(max_length=20, verbose_name='\u8ba1\u7b97\u673a\u8bed\u8a00')),
                ('linenos', models.CharField(max_length=20, verbose_name='\u663e\u793a\u884c\u53f7')),
                ('owner', models.ForeignKey(related_name='snippets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
