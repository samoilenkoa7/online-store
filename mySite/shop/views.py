from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Account, AccountPlatform
from django.db.models import Count
from django.views.generic import DetailView, CreateView
from .forms import EmailtoBuyForm, SortForm
from .telegramm import send_msg


def shop(request):
    sorting = SortForm(request.POST)
    if sorting.is_valid():
        needed_sort = sorting.cleaned_data['sort_form']
        file = Account.objects.all().order_by(needed_sort)
    else:
        file = Account.objects.all()
    data = {
        'file': file,
        'form': sorting,
    }
    return render(request, 'shop/shop.html', data)


def get_platform_view(request, accountplatform_id):
    sorting = SortForm(request.POST)
    platform_item = AccountPlatform.objects.get(pk=accountplatform_id)
    file = Account.objects.filter(platform=accountplatform_id)
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


# class OrderAccount(CreateView):
#     model = Account.objects.all()
#     context_object_name = 'account'
#     form_class = EmailtoBuyForm
#     template_name = 'shop/order.html'
#     success_url = reverse_lazy('success')
#
#     def form_valid(self, form):
#         email = form.cleaned_data['email']
#         name = form.cleaned_data['name']
#         account_id = form.cleaned_data['account_id']
#         message = f'Request from website: {name}, {email}, {account_id}'
#         send_msg(message)
#         return super(OrderAccount, self).form_valid(form)

def account_order(request, account_id):
    account = Account.objects.get(id=account_id)
    if request.method == 'POST':
        form = EmailtoBuyForm(request.POST)
        if form.is_valid():
            form.save()
            send_msg(text=str(form.cleaned_data))
            return redirect('success')
    else:
        form = EmailtoBuyForm
    return render(request, 'shop/order.html', context={'form': form, 'account': account})


def success_order(request):
    return render(request, 'shop/success-order.html')
