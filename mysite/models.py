
# encoding: utf-8
from django.db import models
from django import forms
import django.utils.timezone as timezone
import django.core.files as File
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
import datetime


class classGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name="班级名字", default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "班级"
        verbose_name_plural = "班级"

class student(models.Model):
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
        verbose_name = verbose_name_plural = "家长报名表"

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

class course(models.Model):
    url = models.FileField(upload_to="course", blank=False)
    title = models.CharField(max_length=32, verbose_name="图片标题",  blank=True)
    description = models.CharField(max_length=256, verbose_name="描述信息", blank=True)
    active = models.BooleanField(verbose_name="是否发布", default=True)

    class Meta:
        verbose_name = "课程图片及介绍"
        verbose_name_plural = "课程图片及介绍"

class Article(models.Model):
    title = models.CharField(max_length=32, verbose_name="文章标题")
    cname = models.ForeignKey(classGroup, verbose_name="班级")
    content = RichTextUploadingField(verbose_name='正文')
    class Meta:
        verbose_name = "每日班级图片"
        verbose_name_plural = "每日班级图片"

# class ArticleForm(forms.ModelForm):
#     brief = forms.CharField(widget=CKEditorUploadingWidget())
#     class Meta:
#         model = Article
#         fields = "__all__"
