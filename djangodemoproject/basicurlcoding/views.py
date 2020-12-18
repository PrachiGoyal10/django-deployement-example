from django.shortcuts import render


# Create your views here.
def index(request):
    contexdict = {'text': 'Prachi Goyal','num':1300000}
    return render(request,'basicurl/index.html',contexdict)

def base(request):
    return render(request,'basicurl/base.html')

def other(request):
    return render(request,'basicurl/other.html')

def relative(request):
    return render(request,'basicurl/relative_url_templates.html')

