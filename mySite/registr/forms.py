from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Your email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
    username = forms.CharField(label='Username', max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    password1 = forms.CharField(label='Create password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    password = forms.CharField(label='Your password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))