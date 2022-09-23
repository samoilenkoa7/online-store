from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from .forms import UserRegisterForm, UserLoginForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Register complete')
            return redirect('shop')
        else:
            messages.error(request, 'Registration Error')
    else:
        form = UserRegisterForm()
    return render(request, 'registr/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('shop')
        else:
            messages.error(request, 'Login Error')
    else:
        form = UserLoginForm()
    return render(request, 'registr/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')