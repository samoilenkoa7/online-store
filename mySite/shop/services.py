from .telegramm import send_msg
from .models import Account

from django.core.mail import send_mail
from django.core.paginator import Paginator


def send_bil_to_user_and_send_notif_to_tg(user, form) -> None:
    """Function that sends email and telegram notification after account order"""
    send_msg(text=f'{user.email} ordered account with ID {form.cleaned_data["account_id"]}')
    send_mail(f'Dear {user.username}, Account ID ' + form.cleaned_data["account_id"],
              f'Your order with ID - {form.cleaned_data["account_id"]} is preparing', 'samoilenkoa7@ukr.net',
              [user.email], fail_silently=False)


def pagination_for_shop_items(model: object, amount_per_page: int, request: dict):
    """Function that provides pagination for shop page"""
    paginator = Paginator(model, amount_per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return page_obj
