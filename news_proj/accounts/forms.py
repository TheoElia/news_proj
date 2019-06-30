from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # specify fields you want to show in HTML form here
        # Other necessary field for registering a user may
        # automatically included by django
        # This happens with user creation forms
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # specify fields you want to show in HTML form here
        fields = ('username', 'email' )