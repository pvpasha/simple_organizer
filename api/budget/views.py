import logging

from rest_framework import status, exceptions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView, ListAPIView, RetrieveAPIView,
                                     RetrieveUpdateAPIView, UpdateAPIView)
from django_filters.rest_framework import DjangoFilterBackend

from django.core import exceptions
from .models import Currency, CategoryBudget, BudgetAccount, Invoice
from .serializers import CurrencySerializer, CategoryBudgetSerializer, BudgetAccountSerializer, InvoiceSerializer
from .filters import InvoiceFilter, BudgetAccountFilter


logger = logging.getLogger(__name__)


class CurrencyListView(ListAPIView):        # >> /currency-list/
    serializer_class = CurrencySerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'owner'

    def get_queryset(self):
        try:
            return Currency.objects.filter(owner=self.request.user.id)
        except exceptions.ObjectDoesNotExist:
            logger.error('Object not found for user with ID #%s for currency_list_view' % self.request.user.id)
            raise exceptions.NotFound('Object with your ID %s NotFound' % self.request.user.id)


class CurrencyRetUpdView(RetrieveUpdateAPIView):        # >> /currency<pk>/
    serializer_class = CurrencySerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            instance = Currency.objects.filter(owner=self.request.user.id)
            return instance
        except exceptions.ObjectDoesNotExist:
            logger.error('Not found object with ID #%s and user ID #%s for currency_retrieve_update'
                         % self.kwargs['pk'], self.request.user.id)
            raise exceptions.NotFound('Object not found')

    def update(self, request, *args, **kwargs):
        pass


class CategoryBudgetListView(ListAPIView):      # >> /category-list/
    serializer_class = CategoryBudgetSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'owner'

    def get_queryset(self):
        try:
            return CategoryBudget.objects.filter(owner=self.request.user.id)
        except exceptions.ObjectDoesNotExist:
            logger.error('Object not found for user with ID #%s for category_budget_list_view' % self.request.user.id)
            raise exceptions.NotFound('Object with your ID %s NotFound' % self.request.user.id)


class CategoryBudgetRetUpdView(RetrieveUpdateAPIView):        # >> /category<pk>/
    serializer_class = CategoryBudgetSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            return CategoryBudget.objects.filter(owner=self.request.user.id)
        except exceptions.ObjectDoesNotExist:
            logger.error('CategoryBudget for user %s and ID #%s not found for category_budget_retrieve_update_view'
                         % self.request.user.email, self.kwargs['pk'])
            raise exceptions.NotFound('Category with ID not found')

    def update(self, request, *args, **kwargs):
        pass


class BudgetAccountListView(ListAPIView):       # >> /account-list/
    serializer_class = BudgetAccountSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = BudgetAccountFilter

    def get_queryset(self):
        try:
            return BudgetAccount.objects.filter(owner=self.request.user.id)
        except exceptions.ObjectDoesNotExist:
            logger.error('Object not found for user with ID #%s for budget_account_list_view' % self.request.user.id)
            raise exceptions.NotFound('Object with your ID %s NotFound' % self.request.user.id)


class BudgetAccountRetUpdView(RetrieveUpdateAPIView):       # >> /account<pk>/
    serializer_class = BudgetAccountSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            return BudgetAccount.objects.filter(owner=self.request.user.id)
        except exceptions.ObjectDoesNotExist:
            logger.error('BudgetAccount for user %s and ID #%s not found for budget_account_retrieve_update_view'
                         % self.request.user.email, self.kwargs['pk'])
            raise exceptions.NotFound('Account with ID not found')

    def update(self, request, *args, **kwargs):
        pass


class InvoiceListView(ListAPIView):     # >> /invoice-list/
    serializer_class = InvoiceSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = InvoiceFilter

    def get_queryset(self):
        try:
            return Invoice.objects.filter(owner=self.request.user.id)
        except exceptions.ObjectDoesNotExist:
            logger.error('Object not found for user with ID #%s for invoice_list_view' % self.request.user.id)
            raise exceptions.NotFound('Object with your ID %s NotFound' % self.request.user.id)


class InvoiceRetUpdView(RetrieveUpdateAPIView):     # >> /invoice<pk>/
    serializer_class = InvoiceSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            instance = Invoice.objects.filter(owner=self.request.user.id)
            return instance
        except exceptions.NotFound:
            logger.error('Invoice ID #%s and user %s not found for invoice_retrieve_update_view'
                         % self.kwargs['pk'], self.request.user.email)
            raise exceptions.NotFound('Invoice with ID #%s not found' % self.kwargs['pk'])
