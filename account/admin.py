from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .form import CustomUserChangeForm, CustomUserCreationForm
from .models import customUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = customUser


admin.site.register(customUser, CustomUserAdmin)
