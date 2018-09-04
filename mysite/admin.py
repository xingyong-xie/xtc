# encoding: utf-8
from django.contrib import admin
from mysite.models import student, picture, classGroup
from django.utils.safestring import mark_safe

@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['parent_name', "name", 'phone','birth', 'password']
    list_per_page = 25
    search_fields =('name', 'phone',) #搜索字段


@admin.register(classGroup)
class ClassGroupAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(picture)
class PictureAdmin(admin.ModelAdmin):
    def admin_thumb(self, obj):
        return mark_safe('<img src="%s" height="50px" width="50px" />' % (obj.url.url,))
    admin_thumb.short_description = 'Thumb'
    admin_thumb.allow_tags = True

    list_display = ['admin_thumb' ,'title', 'description', "active"]
    list_per_page = 25
    ordering = ('-modify_date', )
    list_filter =('create_date', ) #过滤器
    search_fields =('create_date', ) #搜索字段
    date_hierarchy = 'create_date'   # 详细时间分层筛选　
