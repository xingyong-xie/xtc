from django.conf.urls import include,url
from django.contrib import admin
from mysite.views import template_as_view,signup_submit_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', template_as_view("index.html")),
    url(r'^index_demo.html', template_as_view("index-demo.html")),
    url(r'^signup.html', template_as_view("signup.html")),
    url(r'^register', signup_submit_view()),
    url(r'^admin/', include(admin.site.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

