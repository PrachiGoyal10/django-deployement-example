from django.shortcuts import render
from django.http import HttpResponse
# from first_app.models import User
from first_app.forms import newuserform



# Create your views here.

def index(request):
    my_dict = {'insertme' : "Heloo i am from views .py...Ok i have created seprated folder for first_App"}
    return render(request,'first_app/index.html',context = my_dict)

def user(request):
    #ud = User.objects.order_by('first_name')
    #userdata = {'user':ud}
    form = newuserform()
    if request.method == "POST":
        form = newuserform(request.POST)
        if form.is_valid():
            print("Validation Success")
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")

    return render(request,'first_app/fstapp_form.html',{'form' : form} )