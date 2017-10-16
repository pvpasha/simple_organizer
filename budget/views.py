from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import OrganizerUser
from .models import CategoryBudget, Currency, AccountType, BudgetAccount, Invoice
from .serializers import (CategoryBudgetListSerializer, CategoryBudgetSerializer, CurrencySerializer,
                          CurrencyListSerializer, AccountTypeListSerializer, AccountTypeSerializer,
                          BudgetAccountListSerializer, BudgetAccountSerializer, InvoiceSerializer,
                          InvoiceListSerializer)


class CategoryBudgetItemView(RetrieveAPIView):
    queryset = CategoryBudget.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CategoryBudgetSerializer
    lookup_field = 'title'


class CategoryBudgetListViewSet(ListCreateAPIView):
    queryset = CategoryBudget.objects.all()          ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = CategoryBudgetListSerializer

    def post(self, request):
        get_owner = request.data['owner']
        get_title = request.data['title']
        try:
            user = OrganizerUser.objects.get(pk=get_owner)
            cat_budget_item = CategoryBudget.objects.create(owner=user, title=get_title)
            serialized_data = self.get_serializer(cat_budget_item)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class CurrencyItemView(RetrieveAPIView):
    queryset = Currency.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CurrencySerializer
    lookup_field = 'short_name'


class CurrencyListViewSet(ListCreateAPIView):
    queryset = Currency.objects.all()          ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = CurrencyListSerializer

    def post(self, request):
        get_owner = request.data['owner']
        get_name = request.data['name']
        get_short_name = request.data['short_name']
        try:
            user = OrganizerUser.objects.get(pk=get_owner)
            currency_item = Currency.objects.create(owner=user, name=get_name, short_name=get_short_name)
            serialized_data = self.get_serializer(currency_item)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class AccountTypeItemView(RetrieveAPIView):
    queryset = AccountType.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AccountTypeSerializer
    lookup_field = 'short_name'


class AccountTypeListViewSet(ListCreateAPIView):
    queryset = AccountType.objects.all()          ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = AccountTypeListSerializer

    def post(self, request):
        get_owner = request.data['owner']
        get_currency = request.data['currency']
        get_name = request.data['name']
        get_short_name = request.data['short_name']
        try:
            user = OrganizerUser.objects.get(pk=get_owner)
            account_type_item = AccountType.objects.create(owner=user, currency=get_currency, name=get_name,
                                                       short_name=get_short_name)
            serialized_data = self.get_serializer(account_type_item)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class BudgetAccountItemView(RetrieveAPIView):
    queryset = BudgetAccount.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = BudgetAccountSerializer
    lookup_field = 'short_name'


class BudgetAccountListViewSet(ListCreateAPIView):
    queryset = BudgetAccount.objects.all()          ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = BudgetAccountListSerializer

    def post(self, request):
        get_owner = request.data['owner']
        get_currency = request.data['currency']
        get_name = request.data['name']
        get_short_name = request.data['short_name']
        get_amount = request.data['amount']
        get_account_type = request.data['account_type']
        try:
            user = OrganizerUser.objects.get(pk=get_owner)
            budget_account_item = BudgetAccount.objects.create(owner=user, currency=get_currency, name=get_name,
                                                               short_name=get_short_name, amount=get_amount,
                                                               account_type=get_account_type)
            serialized_data = self.get_serializer(budget_account_item)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class InvoiceItemView(RetrieveAPIView):
    queryset = Invoice.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = InvoiceSerializer


class InvoiceListViewSet(ListCreateAPIView):
    queryset = Invoice.objects.all()          ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = InvoiceListSerializer

    def post(self, request):
        get_owner = request.data['owner']
        get_currency = request.data['currency']
        get_name = request.data['name']
        get_transaction_type = request.data['transaction_type']
        get_category = request.data['category']
        get_description = request.data['description']
        get_budget_account = request.data['budget_account']
        try:
            user = OrganizerUser.objects.get(pk=get_owner)
            invoice_item = Invoice.objects.create(owner=user, currency=get_currency, name=get_name,
                                                  transaction_type=get_transaction_type, category=get_category,
                                                  description=get_description, budget_account=get_budget_account)
            serialized_data = self.get_serializer(invoice_item)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
