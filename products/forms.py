from dataclasses import fields
from django import forms
from .models import Login
#label 
#initial
#disabled
#help_text
#widget >> forms.passwordInput
#required

# class LoginForm (forms.Form):
#     username = forms.CharField(max_length=50)
#     password = forms.CharField(max_length=50)

#updated 
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login 
        fields = '__all__'