from django.contrib.auth.views  import LoginView

from django.http import HttpResponse, HttpRequest

from django.shortcuts import render

from django.urls import reverse

from .forms import *

class CustomLoginView(LoginView):
    
    authentication_form = CustomAuthenticationForm
    tempplate_name = 'Proyecto_final/login.html'