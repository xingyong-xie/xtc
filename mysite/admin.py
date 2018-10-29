# encoding: utf-8
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from mysite.models import onlineQuery,picture,VmaigUser
from django.utils.safestring import mark_safe
from mysite.forms import VmaigUserCreationForm
from mysite import models

@admin.register(onlineQuery)
class onlineQueryAdmin(admin.ModelAdmin):
    list_display = ['parent_name', "name", 'phone','birth', 'info']
    list_per_page = 25
    search_fields =('name', 'phone', 'info',) #搜索字段

@admin.register(picture)
class PictureAdmin(admin.ModelAdmin):
    def admin_thumb(self, obj):
        return mark_safe('<img src="%s" height="50px" width="50px" />' % (obj.url.url,))
    admin_thumb.short_description = 'Thumb'
    admin_thumb.allow_tags = True

    list_display = ['admin_thumb' ,'title', 'description', "active"]
    list_per_page = 25

# Register your models here.
class VmaigUserAdmin(UserAdmin):
    add_form = VmaigUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )
    fieldsets = (
        (u'基本信息', {'fields': ('username', 'password', 'email')}),
        (u'权限', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (u'时间信息', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.unregister(Group)
admin.site.register(VmaigUser, VmaigUserAdmin)
admin.site.register(models.ClassList)

@admin.register(models.CourseRecord)
class CourseRecordAdmin(admin.ModelAdmin):
    list_display = ['__str__','from_class',]
    list_filter =('from_class', ) #过滤器
