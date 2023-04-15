from django.shortcuts import render
from django.views import generic
from .form import UserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from .models import customUser


class SignupView(generic.CreateView):
    form_class = UserCreationForm
    model = customUser
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


