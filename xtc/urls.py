from django.conf.urls import include,url
from django.contrib import admin
from mysite.views import template_as_view,signup_submit_view,courses_view,about_view
from django.conf import settings
from django.conf.urls.static import static
from mysite.views import UserControl
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', template_as_view("index.html")),
    url(r'^courses.html', courses_view("courses.html")),
    url(r'^about.html', about_view("about.html")),
    url(r'^index_demo.html', template_as_view("index-demo.html")),
    url(r'^signup.html', signup_submit_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^usercontrol/(?P<slug>\w+)$', UserControl.as_view()),
    url(r'^login.html', TemplateView.as_view(template_name="login.html"), name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

