# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailHandler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server', models.CharField(max_length=50, verbose_name='\u90ae\u4ef6\u670d\u52a1\u5668\u5730\u5740\uff08IP/Host\uff09')),
                ('port', models.IntegerField(verbose_name='\u90ae\u4ef6\u670d\u52a1\u7aef\u53e3')),
                ('username', models.CharField(max_length=50, verbose_name='\u767b\u5f55\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=200, verbose_name='\u767b\u5f55\u5bc6\u7801')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('changed_time', models.DateTimeField(auto_now=True)),
                ('tos', models.CharField(help_text='\u5206\u53f7\u9694\u5f00\u7684\u591a\u4e2a\u90ae\u4ef6\u5730\u5740', max_length=500, verbose_name='\u63a5\u53d7\u8005\u5217\u8868')),
                ('subject', models.CharField(max_length=300, verbose_name='\u90ae\u4ef6\u6807\u9898')),
                ('context', models.TextField(verbose_name='\u90ae\u4ef6\u5185\u5bb9')),
            ],
        ),
    ]
