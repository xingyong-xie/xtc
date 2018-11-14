
# encoding: utf-8
from django.db import models
from django import forms
import django.utils.timezone as timezone
import django.core.files as File
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField
import datetime


class onlineQuery(models.Model):
    name = models.CharField(max_length=32, verbose_name="宝贝姓名")
    parent_name = models.CharField(max_length=32, verbose_name="家长姓名")
    address = models.CharField(max_length=128, verbose_name="家庭地址",  default="")
    phone = models.CharField(max_length=16, verbose_name="电话号码", default="")
    info = models.CharField(max_length=128, verbose_name="备注信息",  default="")
    default_data = datetime.date(2016, 1, 1)
    birth = models.DateField("出生年月", default=default_data)
    create_date = models.DateTimeField('创建日期', auto_now_add=True)
    modify_date = models.DateTimeField('修改日期', auto_now=True)

    class Meta:
        ordering = ('-modify_date',)
        verbose_name = verbose_name_plural = "线上咨询表"

    def get_username(self):
        return self.name

class picture(models.Model):
    url = models.FileField(upload_to="school", blank=False)
    title = models.CharField(max_length=32, verbose_name="图片标题",  blank=True)
    description = models.CharField(max_length=256, verbose_name="描述信息", blank=True)
    active = models.BooleanField(verbose_name="是否发布", default=True)

    class Meta:
        verbose_name = "校区图片及介绍"
        verbose_name_plural = "校区图片及介绍"

class VmaigUser(AbstractUser):
    img = models.CharField(max_length=200, default='/static/tx/default.jpg',
                           verbose_name=u'头像地址')
    intro = models.CharField(max_length=200, blank=True, null=True,
                             verbose_name=u'简介')

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"


class CourseRecord(models.Model):
    '''上课记录'''
    from_class = models.ForeignKey("ClassList",verbose_name="班级")
    day_num = models.PositiveSmallIntegerField(verbose_name="第几节(天)")
    #teacher = models.ForeignKey("UserProfile", verbose_name="老师")
    #has_homework = models.BooleanField(default=True, verbose_name="是否有家庭作业")
    #homework_title = models.CharField(max_length=128,blank=True,null=True,verbose_name="作业标题")
    #homework_content = models.TextField(blank=True,null=True, verbose_name="作业内容")
    #outline = models.TextField(blank=True,null=True, verbose_name="本节课程大纲")
    record_title = models.CharField(max_length=128,blank=True,null=True,verbose_name="课程记录标题")
    record_content = RichTextUploadingField(verbose_name='课程详细图文')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.from_class, self.day_num)

    class Meta:
        unique_together = ("from_class", "day_num")
        verbose_name_plural = "班级课程记录"

class ClassList(models.Model):
    '''班级表'''
    class_name = models.CharField(max_length=128,blank=True,null=True,verbose_name="班级名称")
    class_content = models.TextField(blank=True,null=True, verbose_name="班级信息")

    def __str__(self):
        return "%s" %(self.class_name)

    class Meta:
        verbose_name = verbose_name_plural = "班级信息"


class ClassMemeber(models.Model):
    from_class = models.ForeignKey("ClassList",verbose_name="班级")
    user = models.ForeignKey("VmaigUser",verbose_name="用户")

    def __str__(self):
        return "%s %s" %(self.from_class, self.user)
    class Meta:
        verbose_name = verbose_name_plural = "班级成员"