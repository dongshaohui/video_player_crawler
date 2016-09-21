#coding=utf-8
from django.db import models

# Create your models here.

class porn_video_info(models.Model):
	number = models.IntegerField(default = 0,verbose_name=u'编号') # 视频编号
	desc = models.CharField(default='',verbose_name=u'介绍',max_length=255) # 介绍
	link = models.CharField(default='',verbose_name=u'链接地址',max_length=255) # 链接地址
	thumb = models.CharField(default='',verbose_name=u'缩略图地址',max_length=255) # 缩略图地址