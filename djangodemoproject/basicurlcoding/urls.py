from django.conf.urls import url
from basicurlcoding import views

# TEMPLATE TAGGING
app_name = 'basicurlcoding'

urlpatterns = [
    url(r'^relative/$', views.relative, name="relative"),
    url(r'^other/$', views.other, name="other"),
]
