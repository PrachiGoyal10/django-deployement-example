from django import forms
from first_app.models import User



class newuserform(forms.ModelForm):

    class Meta:
        model = User
        fields =  '__all__'


