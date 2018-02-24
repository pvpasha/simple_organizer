from rest_framework import serializers

from .models import Currency, CategoryBudget, BudgetAccount, Invoice


class CurrencySerializer(serializers.ModelSerializer):          # or StringRelatedField [owner email]
    owner = serializers.PrimaryKeyRelatedField(read_only=True)  # or PrimaryKeyRelatedField [owner id]

    class Meta:
        model = Currency
        fields = '__all__'


class CategoryBudgetSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CategoryBudget
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
