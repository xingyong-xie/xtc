from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import template_as_view

urlpatterns = [
    url(r'^$', template_as_view("index.html")),
    url(r'^admin/', include(admin.site.urls)),
]
