from django.contrib import admin

# Register your models here.
from AppTwo.models import Webpage,Topic,Accessrecord

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Accessrecord)


