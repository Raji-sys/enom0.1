from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from staff.models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2','first_name','last_name']


class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']


