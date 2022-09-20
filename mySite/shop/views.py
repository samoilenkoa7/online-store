from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Account, AccountPlatform
from django.db.models import F
from django.views.generic import DetailView, CreateView, ListView
from .forms import EmailtoBuyForm, SortForm
from .telegramm import send_msg


def shop(request):
    sorting = SortForm(request.POST)
    if sorting.is_valid():
        needed_sort = sorting.cleaned_data['sort_form']
        file = Account.objects.all().order_by(needed_sort).select_related('platform')
    else:
        file = Account.objects.all().select_related('platform')
    data = {
        'file': file,
        'form': sorting,
    }
    return render(request, 'shop/shop.html', data)


def get_platform_view(request, accountplatform_id):
    sorting = SortForm(request.POST)
    platform_item = AccountPlatform.objects.get(pk=accountplatform_id)
    file = Account.objects.filter(platform=accountplatform_id).select_related('platform')
    data = {
        'file': file,
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
        return redirect('success')


def success_order(request):
    return render(request, 'shop/success-order.html')
