# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from crm import models

admin.site.register(models.CustomerFollowUp)
admin.site.register(models.Enrollment)
admin.site.register(models.Course)
admin.site.register(models.ClassList)
admin.site.register(models.Branch)
admin.site.register(models.Role)
admin.site.register(models.Payment)
admin.site.register(models.StudyRecord)
admin.site.register(models.Tag)
# Register your models here.
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','wechat_name','source','consultant','content','status','date')
    list_filter = ('source','consultant','date')
    search_fields = ('wechat_name','name')
    #raw_id_fields = ('consult_course',)
    filter_horizontal = ('tags',)
    list_editable = ('status',)


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','name')


@admin.register(models.CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user','customer')


@admin.register(models.CourseRecord)
class CourseRecordAdmin(admin.ModelAdmin):
    list_display = ['__str__','from_class',]
    list_filter =('from_class', ) #过滤器


# admin.site.register(models.Customer,CustomerAdmin)
# admin.site.register(models.UserProfile,UserProfileAdmin)