from rest_framework import serializers

from .models import CategoryBudget, Currency, AccountType, BudgetAccount, Invoice


class CategoryBudgetSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)          # or PrimaryKeyRelatedField [owner id]
                                                                        # or StringRelatedField [owner email]
    class Meta:
        model = CategoryBudget
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Currency
        fields = '__all__'


class AccountTypeSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = AccountType
        fields = '__all__'


class BudgetAccountSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = BudgetAccount
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'
