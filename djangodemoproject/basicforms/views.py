from django.shortcuts import render
from . import forms # = from basicform import forms

# Create your views here.
def index(request):

    return render(request,'basic_form/basicform.html')

def form_name_view(request):
    form  = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Validation Success")
            print("NAME: ",form.cleaned_data['name'])
            print("email: ",form.cleaned_data['email'])
            print("text: ",form.cleaned_data['text'])

    return render(request,'basic_form/form_page.html',{'form': form})
