from rest_framework import serializers
from account.models import Account


class  AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ("password",)

class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('password', 'username', 'first_name', 'last_name', 'photo', 'gender')



