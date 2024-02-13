from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

# Login
class CustomAuthenticationForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class":"form-control"}),
             "password": forms.PasswordInput(attrs={"class":"form-control"}),
             
                      }
   