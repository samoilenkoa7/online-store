from rest_framework import serializers
from shop.models import Account


class AccountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
