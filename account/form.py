from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import customUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = customUser
        fields = UserCreationForm.Meta.fields + ('age',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = customUser
        fields = UserChangeForm.Meta.fields


# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = customUser
#         fields = ('username', 'password1', 'password2')
