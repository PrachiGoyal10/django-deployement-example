from django import forms
from django.core import validators

def z_char_checker(value):# value is must to recognize as a validator
    if value[0].lower() != 'z':
        raise forms.ValidationError("Needs too start with Z")



class FormName(forms.Form):
    #3rd method (customized validators)
    name = forms.CharField(validators=[z_char_checker])
    email = forms.EmailField()
    #4th method
    verify_email = forms.EmailField()
    text =  forms.CharField(widget=forms.Textarea)

    #2nd method
    # botcahtcher = forms.CharField(required=False,
    #                               widget=forms.HiddenInput,
    #                               validators= [validators.MaxLengthValidator(0)]
    #                                )

    #1st meethod
    # botcahtcher = forms.CharField(required=False,
    #                               widget=forms.HiddenInput)
    #
    # def clean_botcahtcher(self):
    #     botcahtcher = self.cleaned_data['botcahtcher']
    #     if botcahtcher:
    #         raise forms.ValidationError(" Gotcha Boo !")
    #     return botcahtcher

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        # vmail = all_clean_data['verify_email']
        # if email != vmail:
        #     raise forms.ValidationError("Wrong e-mail")



