from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.serializers import AccountModelSerializer
from api.pagination import ItemSetPagination

from shop.models import Account


class AccountListAPIView(generics.ListAPIView):
    queryset = Account.objects.all().select_related('platform')
    serializer_class = AccountModelSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = ItemSetPagination
