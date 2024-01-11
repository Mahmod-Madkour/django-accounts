from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        # 'f_name', 'l_name', 'phone', 'country', 'city',
        fields = ['username', 'email', 'password1', 'password1']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # 'f_name', 'l_name', 'phone', 'country', 'city',
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number']