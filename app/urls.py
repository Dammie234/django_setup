from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="hello.html"))
)
