from django.shortcuts import render, redirect
from django.db.models import F
from django.views.generic import DetailView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.contrib import messages

from .forms import EmailtoBuyForm, SortForm, CreateAccount
from .models import Account, AccountPlatform
from .telegramm import send_msg


def shop(request):
    sorting = SortForm(request.POST)
    if sorting.is_valid():
        needed_sort = sorting.cleaned_data['sort_form']
        file = Account.objects.all().order_by(needed_sort).select_related('platform')
        paginator = Paginator(file, 1)
        page_number = request.GET.get('page', 9)
        page_obj = paginator.get_page(page_number)
    else:
        file = Account.objects.all().select_related('platform')
        paginator = Paginator(file, 1)
        page_number = request.GET.get('page', 9)
        page_obj = paginator.get_page(page_number)
    data = {
        'file': page_obj,
        'form': sorting,
    }
    return render(request, 'shop/shop.html', data)


def get_platform_view(request, accountplatform_id):
    sorting = SortForm(request.POST)
    platform_item = AccountPlatform.objects.get(pk=accountplatform_id)
    file = Account.objects.filter(platform=accountplatform_id).select_related('platform')
    paginator = Paginator(file, 9)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    data = {
        'file': page_obj,
        'form': sorting,
        'platform_item': platform_item,
    }
    return render(request, 'shop/shop.html', data)


class ProductView(DetailView):
    model = Account
    template_name = 'shop/product.html'
    context_object_name = 'account'

    def get_object(self, queryset=None):
        """this function allows
        me to control popularity
         of product, calculating views"""
        product = super().get_object()
        product.views = F('views') + 1
        product.save()
        return product


class AccountOrder(CreateView):
    form_class = EmailtoBuyForm
    template_name = 'shop/order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['account'] = Account.objects.get(id=self.kwargs['account_id'])
        return context

    def form_valid(self, form):
        send_msg(text=str(form.cleaned_data))
        send_mail(f'Dear {self.request.user.username}, Account ID ' + form.cleaned_data["account_id"],
                  f'Your order with ID - {form.cleaned_data["account_id"]} is preparing', 'samoilenkoa7@ukr.net',
                  [self.request.user.email], fail_silently=False)
        messages.success(self.request, 'Account successfully ordered')
        return redirect('success')


class CreateAccount(LoginRequiredMixin, CreateView):
    form_class = CreateAccount
    template_name = 'shop/add-account.html'
    login_url = '/admin/'
    success_url = 'shop'


def success_order(request):
    return render(request, 'shop/success-order.html')
