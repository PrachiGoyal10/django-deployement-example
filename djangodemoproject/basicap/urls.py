from basicap import views
from django.conf.urls import url

#TEMPLATE URLS
app_name = 'basic_ap'

urlpatterns =[
    url(r'^register/$',views.register,name='register'),
    url(r'^login',views.user_login,name='user_login'),
]

