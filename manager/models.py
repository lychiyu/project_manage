# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class ProjectInfo(models.Model):
    STATUS = (
        (0, '删除'),
        (1, '正常'),
    )
    name = models.CharField(max_length=30, verbose_name='项目名(英文)')
    display_name = models.CharField(max_length=60, verbose_name='项目显示名')
    status = models.IntegerField('状态', choices=STATUS, default=1)
    remark = models.CharField('备注', max_length=50, blank=True, default='')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __unicode__(self):
        return 'id :' + str(self.id) + '-' + self.display_name

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = verbose_name


class UserInfo(models.Model):
    STATUS = (
        (0, '删除'),
        (1, '正常'),
    )
    name = models.CharField(max_length=30, verbose_name='成员姓名')
    email = models.CharField(max_length=40, verbose_name='成员邮箱')
    status = models.IntegerField('状态', choices=STATUS, default=1)
    remark = models.CharField('备注', max_length=50, blank=True, default='')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __unicode__(self):
        return 'id :' + str(self.id) + '-' + self.name

    class Meta:
        verbose_name = '项目成员'
        verbose_name_plural = verbose_name


class GroupInfo(models.Model):
    STATUS = (
        (0, '删除'),
        (1, '正常'),
    )
    name = models.CharField(max_length=30, verbose_name='项目组名')
    project = models.ForeignKey(ProjectInfo, verbose_name='所属项目')
    members = models.ManyToManyField(UserInfo, verbose_name='项目组成员')
    status = models.IntegerField('状态', choices=STATUS, default=1)
    remark = models.CharField('备注', max_length=50, blank=True, default='')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __unicode__(self):
        return 'id :' + str(self.id) + '-' + self.project.display_name + '-' + self.name

    class Meta:
        verbose_name = '项目组'
        verbose_name_plural = verbose_name
