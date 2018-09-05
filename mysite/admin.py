# encoding: utf-8
from django.contrib import admin
from mysite.models import student,picture,classGroup,course
from django.utils.safestring import mark_safe

@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['parent_name', "name", 'phone','birth', 'info']
    list_per_page = 25
    search_fields =('name', 'phone', 'info',) #搜索字段


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

@admin.register(course)
class CourseAdmin(admin.ModelAdmin):
    def admin_thumb(self, obj):
        return mark_safe('<img src="%s" height="50px" width="50px" />' % (obj.url.url,))
    admin_thumb.short_description = 'Thumb'
    admin_thumb.allow_tags = True

    list_display = ['admin_thumb' ,'title', 'description', "active"]
    list_per_page = 25
