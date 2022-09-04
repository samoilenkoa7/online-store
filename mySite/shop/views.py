from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Account
from django.views.generic import DetailView, CreateView
from .forms import EmailtoBuyForm, SortForm
from .telegramm import send_msg


def shop(request):
    sorting = SortForm(request.POST)
    needed_sort = ''
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


class ProductView(DetailView):
    model = Account
    template_name = 'shop/product.html'
    context_object_name = 'account'


class OrderAccount(CreateView):
    model = Account
    form_class = EmailtoBuyForm
    template_name = 'shop/order.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        name = form.cleaned_data['name']
        account_id = form.cleaned_data['account_id']
        message = f'Request from website: {name}, {email}, {account_id}'
        send_msg(message)
        return super(OrderAccount, self).form_valid(form)


def success_order(request):
    return render(request, 'shop/success-order.html')
