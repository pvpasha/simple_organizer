from rest_framework import serializers

from .models import CategoryBudget, Currency, AccountType, BudgetAccount, Invoice


class CategoryBudgetListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = CategoryBudget
        fields = '__all__'


class CategoryBudgetSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = CategoryBudget
        fields = '__all__'


class CurrencyListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = Currency
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = Currency
        fields = '__all__'


class AccountTypeListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = AccountType
        fields = '__all__'


class AccountTypeSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = AccountType
        fields = '__all__'


class BudgetAccountListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = BudgetAccount
        fields = '__all__'


class BudgetAccountSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = BudgetAccount
        fields = '__all__'


class InvoiceListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = Invoice
        fields = '__all__'
