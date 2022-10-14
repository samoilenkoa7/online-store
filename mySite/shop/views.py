from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import F
from django.views.generic import DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin

from .forms import EmailtoBuyForm, SortForm, CreateAccount
from .models import Account, AccountPics, AccountPlatform
from .services import send_bil_to_user_and_send_notif_to_tg, pagination_for_shop_items, sorting_items_by_platform


def shop(request):
    sorting = SortForm(request.POST)
    if sorting.is_valid():
        file = sorting_items_by_platform(form=sorting)
    else:
        file = Account.objects.all().select_related('platform')
    data = {
        'file': pagination_for_shop_items(model=file, amount_per_page=1, request=request),
        'form': sorting,
    }
    return render(request, 'shop/shop.html', data)


def get_platform_view(request, accountplatform_id):
    sorting = SortForm(request.POST)
    platform_item = AccountPlatform.objects.get(pk=accountplatform_id)
    file = Account.objects.filter(platform=accountplatform_id).select_related('platform')
    data = {
        'file': pagination_for_shop_items(model=file, amount_per_page=1, request=request),
        'form': sorting,
        'platform_item': platform_item,
    }
    return render(request, 'shop/shop.html', data)


class ProductView(DetailView):
    model = Account
    template_name = 'shop/product.html'
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = AccountPics.objects.get(acc=self.kwargs['pk'])
        return context

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
        recipe = form.save(commit=False)
        recipe.user = User.objects.get(id=self.request.user.id)
        recipe.save()
        try:
            send_bil_to_user_and_send_notif_to_tg(user=recipe.user, form=form)
            messages.success(self.request, 'Account successfully ordered')
        except:
            messages.error(self.request, 'Some error occured')
        return redirect('success')


class CreateAccount(PermissionRequiredMixin, CreateView):
    form_class = CreateAccount
    template_name = 'shop/add-account.html'
    login_url = '/admin/'
    success_url = 'shop'


def success_order(request):
    return render(request, 'shop/success-order.html')
