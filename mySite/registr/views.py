from django.contrib import messages
from django.shortcuts import render, redirect
from django.apps import apps
from django.contrib.auth import login, logout
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserView, UserRegisterForm, UserLoginForm
from .models import UserProfile


UserOrder = apps.get_model('shop', 'UserOrder')

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


class UserAccountView(LoginRequiredMixin, ListView):
    template_name = 'registr/account.html'
    context_object_name = 'userorder'
    login_url = 'accountlogin/'

    def get_queryset(self):
        return UserOrder.objects.filter(user=self.request.user).select_related('user')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.request.user.username
        try:
            context['user_profile'] =  UserProfile.objects.get(user=self.request.user)
        finally:
            return context

def change_avatar(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except:
        user_profile = UserProfile.objects.create(user=request.user)
    if request.method == 'POST':
        form = UserView(request.POST, request.FILES)
        if form.is_valid():
            user_profile.avatar = form.cleaned_data['avatar']
            user_profile.save()
            return redirect('account')
    else:
        form = UserView()
    return render(request, 'registr/account.html', context={'form': form, 'user_profile': user_profile})
