from django import forms
from .models import *
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
    def save(self):
        obj= super().save()
        obj.set_password(self.cleaned_data['password'])
        obj.save()
        return obj
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

class loginForm(forms.ModelForm):
    class Meta:
        model=loginModel
        fields='__all__'

class createForm(forms.ModelForm):
    class Meta:
        model= createModel
        fields='__all__'


class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No account found with this email address.")
        return email

