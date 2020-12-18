from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Webpage,Topic,Accessrecord


# Create your views here.

def help(response):
    webpages_list = Accessrecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(response,'AppTwo/index.html',context = date_dict)