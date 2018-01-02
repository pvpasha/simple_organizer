from rest_framework import serializers

from accounts.models import OrganizerUser
from .models import CategoryBudget, Currency, AccountType, BudgetAccount, Invoice


class CategoryBudgetListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = CategoryBudget
        fields = ('__all__')


class CategoryBudgetSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = CategoryBudget
        fields = '__all__'

    def create(self, validated_data):
        pass


class CurrencyListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = Currency
        fields = ('__all__')


class CurrencySerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = Currency
        fields = '__all__'

    def create(self, validated_data):
        pass


class AccountTypeListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = AccountType
        fields = ('__all__')


class AccountTypeSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = AccountType
        fields = '__all__'

    def create(self, validated_data):
        pass


class BudgetAccountListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = BudgetAccount
        fields = ('__all__')


class BudgetAccountSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = BudgetAccount
        fields = '__all__'

    def create(self, validated_data):
        pass


class InvoiceListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = Invoice
        fields = ('__all__')


class InvoiceSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = Invoice
        fields = '__all__'

    # def create(self, validated_data):
    #     user = OrganizerUser.objects.get(pk=self.owner)
    #     return Invoice.objects.create(owner=user.id,
    #                                 title=validated_data.pop('title'),
    #                                 body=validated_data.pop('body'))