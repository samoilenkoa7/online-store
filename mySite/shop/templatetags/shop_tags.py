from django import template
from django.db.models import Count
from ..models import AccountPlatform

register = template.Library()


@register.inclusion_tag('shop/platforms_list.html')
def show_category():
    platforms = AccountPlatform.objects.annotate(cnt=Count('account')).filter(cnt__gt=0)
    return {'platforms': platforms}
