"""djangodemoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
#from AppTwo import views
# from basicforms import views
# from basicurlcoding import views
from basicap import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('admin/', admin.site.urls),
    url('^logout/',views.user_logout,name='logout'),
    url('^special',views.special,name='special'),
    url(r'^basic_ap',include('basicap.urls')),
    # url(r'^basicurlcoding/', include('basicurlcoding.urls')),
    # url(r'^$',views.index,name = 'index2'),
    # url(r'^formpage',views.form_name_view),
    # url(r'^user/', include('first_app.urls')),
    # url(r'^help/', include('AppTwo.urls')),
    # url(r'^add_extension/', include('first_app.urls')),
]
