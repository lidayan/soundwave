# coding: utf-8

from django.db import models

# Create your models here.
class MailHandler(models.Model):
    server = models.CharField(u'邮件服务器地址（IP/Host）', max_length=50)
    port = models.IntegerField(u'邮件服务端口')
    username = models.CharField(u'登录用户名', max_length=50)
    password = models.CharField(u'登录密码', max_length=200)


class Record(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    changed_time = models.DateTimeField(auto_now=True)

    tos = models.CharField(u'接受者列表', max_length=500, help_text=u'分号隔开的多个邮件地址')
    subject = models.CharField(u'邮件标题', max_length=300)
    context = models.TextField(u'邮件内容')
