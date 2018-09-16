# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Customer(models.Model):
    '''客户信息表'''
    name = models.CharField(max_length=32,blank=True,null=True, verbose_name="姓名")
    wechat_id = models.CharField(max_length=64,unique=True,null=True, verbose_name="微信id")
    wechat_name = models.CharField(max_length=64,blank=True,null=True, verbose_name="微信昵称")
    phone = models.CharField(max_length=64,blank=True,null=True,verbose_name="电话号码")
    source_choices = ((0,'转介绍'),
        (1,'门店'),
        (2,'官网'),
        (3,'市场推广'),
        (4,'其它'),
        )

    source = models.SmallIntegerField(choices=source_choices, verbose_name="客源")
    referral_from = models.CharField(verbose_name="转介绍人微信id",max_length=64,blank=True,null=True)
    consult_course = models.ForeignKey("Course",verbose_name="咨询课程")
    consultant = models.ForeignKey("UserProfile",verbose_name="课程顾问")
    content = models.TextField(verbose_name="咨询详情")
    tags = models.ManyToManyField("Tag",blank=True)
    status_choices = ((0,'已报名'),
            (1,'未报名'),
            )
    status = models.SmallIntegerField(choices=status_choices,default=1)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ="客户表"
        verbose_name_plural ="客户表"

class Tag(models.Model):
    name = models.CharField(unique=True,max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"

class CustomerFollowUp(models.Model):
    '''客户跟进表'''
    customer = models.ForeignKey("Customer")
    content = models.TextField(verbose_name="跟进内容")
    consultant = models.ForeignKey("UserProfile",verbose_name="课程顾问")

    intention_choices = ((0,'2周内报名'),
        (1,'1个月内报名'),
        (2,'近期无报名计划'),
        (3,'已在其它机构报名'),
        (4,'已报名'),
        (5,'已拉黑'),
        )
    intention = models.SmallIntegerField(choices=intention_choices)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "<%s : %s>" %(self.customer.name, self.intention)

    class Meta:
        verbose_name = "客户跟进记录"
        verbose_name_plural = "客户跟进记录"

class Course(models.Model):
    '''课程表'''
    name = models.CharField(max_length=64,unique=True,verbose_name="课程名")
    price = models.PositiveSmallIntegerField(verbose_name="单价")
    period = models.PositiveSmallIntegerField(verbose_name="周期(月)")
    outline = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = "课程"

class Branch(models.Model):
    '''校区'''
    name = models.CharField(max_length=128,unique=True)
    addr = models.CharField(max_length=128)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "校区"
        verbose_name_plural = "校区"

class ClassList(models.Model):
    '''班级表'''
    branch = models.ForeignKey("Branch",verbose_name="校区")
    course = models.ForeignKey("Course",verbose_name="课程")
    class_type_choices = ((0,'托管'),
            (1,'培训'),
            )
    class_type = models.SmallIntegerField(choices=class_type_choices,verbose_name="班级类型")
    semester = models.PositiveSmallIntegerField(verbose_name="学期")
    teachers = models.ManyToManyField("UserProfile",verbose_name="老师")
    start_date = models.DateField(verbose_name="开班日期")
    end_date = models.DateField(verbose_name="结业日期",blank=True,null=True)

    def __str__(self):
        return "%s %s %s" %(self.branch,self.course,self.semester)

    class Meta:
        unique_together = ('branch','course','semester')
        verbose_name_plural = "班级"
        verbose_name = "班级"

class CourseRecord(models.Model):
    '''上课记录'''
    from_class = models.ForeignKey("ClassList",verbose_name="班级")
    day_num = models.PositiveSmallIntegerField(verbose_name="第几节(天)")
    teacher = models.ForeignKey("UserProfile", verbose_name="老师")
    has_homework = models.BooleanField(default=True, verbose_name="是否有家庭作业")
    homework_title = models.CharField(max_length=128,blank=True,null=True,verbose_name="作业标题")
    homework_content = models.TextField(blank=True,null=True, verbose_name="作业内容")
    outline = models.TextField(blank=True,null=True, verbose_name="本节课程大纲")
    content = RichTextUploadingField(verbose_name='课程图文记录')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.from_class, self.day_num)

    class Meta:
        unique_together = ("from_class", "day_num")
        verbose_name_plural = "上课记录"


class StudyRecord(models.Model):
    '''学习记录'''
    student = models.ForeignKey("Enrollment")
    course_record = models.ForeignKey("CourseRecord")
    attendance_choices = ((0,'已签到'),
            (1,'迟到'),
            (2,'缺勤'),
            (3,'早退'),
            )
    attendance = models.SmallIntegerField(choices=attendance_choices,default=0, verbose_name="考勤")
    score_choices = ((100,"A+"),
            (90,"A"),
            (85,"B+"),
            (80,"B"),
            (75,"B-"),
            (70,"C+"),
            (60,"C"),
            (40,"C-"),
            (0,"N/A"),
            )
    score = models.SmallIntegerField(choices=score_choices,default=0, verbose_name="成绩")
    memo = models.TextField(blank=True,null=True, verbose_name="备忘录")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s %s %s" %(self.student,self.course_record,self.score)

    class Meta:
        unique_together = ('student','course_record')
        verbose_name_plural = "学习记录"


class Enrollment(models.Model):
    '''报名表'''
    customer = models.ForeignKey("Customer",verbose_name="客户")
    enrolled_class = models.ForeignKey("ClassList",verbose_name="所报班级")
    consultant = models.ForeignKey("UserProfile",verbose_name="课程顾问")
    contract_agreed = models.BooleanField(default=False,verbose_name="学员已同意合同条款")
    contract_approved = models.BooleanField(default=False,verbose_name="合同已审核")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.customer,self.enrolled_class)

    class Meta:
        unique_together = ("customer","enrolled_class")
        verbose_name_plural = "报名表"

class Payment(models.Model):
    '''缴费记录'''
    customer = models.ForeignKey("Customer")
    course = models.ForeignKey("Course",verbose_name="所报课程")
    amount = models.PositiveIntegerField(verbose_name="数额",default=500)
    consultant = models.ForeignKey("UserProfile", verbose_name="课程顾问")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.customer,self.amount)

    class Meta:
        verbose_name_plural = "缴费记录"

class UserProfile(models.Model):
    '''员工'''
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    roles = models.ManyToManyField("Role",blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ="员工"
        verbose_name_plural = "员工"

class CustomerProfile(models.Model):
    '''客户登陆'''
    customer = models.ForeignKey("Customer")
    user = models.OneToOneField(User)

    def __str__(self):
        return "%s" % (self.customer.name)

    class Meta:
        verbose_name ="客户登陆授权"
        verbose_name_plural = "客户登陆授权"


class Role(models.Model):
    '''角色表'''
    name = models.CharField(max_length=32,unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "角色"





