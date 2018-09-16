# encoding: utf-8

from os import path
from django.apps import AppConfig
from django.contrib import admin

def get_current_app_name(file):
    return path.dirname(file).replace('\\', '/').split('/')[-1]

class XtcNameConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = u"小天才CRM"

default_app_config = get_current_app_name(__file__) + '.__init__.XtcNameConfig'