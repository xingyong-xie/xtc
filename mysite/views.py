# encoding: utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from mysite.models import student, picture
from django.conf import settings
from django.views.generic.base import TemplateView


def template_as_view(template_name):
    def view(request):
        list = {}
        list['picture_list'] = picture.objects.filter(active=True)
        return render(request, template_name, list)
    return view


def signup_submit_view():
    def view(request):
        if request.method == "POST":  # 判断是不是POST,如果是POST,准备保存修改
            s = student()
            print request.POST
            s.address = request.POST[u'address']
            s.name = request.POST[u'name']
            s.phone = request.POST[u'phone']
            s.birth = request.POST[u'birth']
            s.parent_name = request.POST[u'parent']

            # 接下来对这个form进行验证
            # if form.is_valid():
            s.save()
            return render(request, "signup.html", {})
    return view
